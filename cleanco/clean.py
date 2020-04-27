"""Functions to help clean & normalize business names.

See http://www.unicode.org/reports/tr15/#Normalization_Forms_Table for details
on Unicode normalization and the NFKD normalization used here.

Basic usage:

>> terms = prepare_terms()
>> basename("Daddy & Sons, Ltd.", terms, prefix=True, middle=True, suffix=True)
Daddy & Sons

"""

import functools
import operator
from collections import OrderedDict
import re
import unicodedata
from iso20275 import ElfEntry


tail_removal_rexp = re.compile(r"[^\.\w]+$", flags=re.UNICODE)


def get_unique_terms():
    "retrieve all unique terms from termdata definitions"
    terms = []

    for elf_code, values in Elf.items():
        entity_codes = Elf[elf_code][0].local_abbreviations
        if ";" in entity_codes:
            split = entity_codes.split(';')
            for split_item in split:
                terms.append(split_item)
        else:
            terms.append(entity_codes)

    terms = filter(None, terms)
    terms = list(filter(None, terms))
    return (terms)


def normalize_terms(terms):
    "normalize terms"
    return (unicodedata.normalize("NFKD", t.casefold()) for t in terms)


def strip_tail(name):
    "get rid of all trailing non-letter symbols except the dot"
    match = re.search(tail_removal_rexp, name)
    if match is not None:
        name = name[: match.span()[0]]
    return name


def normalized(text):
    "caseless Unicode normalization"
    return unicodedata.normalize("NFKD", text.casefold())


def prepare_terms():
    "construct an optimized term structure for basename extraction"
    terms = get_unique_terms()
    nterms = normalize_terms(terms)
    ntermparts = (t.split() for t in nterms)
    sntermparts = sorted(ntermparts, key=len, reverse=True)
    return [(len(tp), tp) for tp in sntermparts]


def basename(name, terms, suffix=True, prefix=False, middle=False, **kwargs):
    "return cleaned base version of the business name"

    name = strip_tail(name)
    nparts = name.split()
    nname = normalized(name)
    nnparts = nname.split()
    nnsize = len(nnparts)

    if suffix:
        for termsize, termparts in terms:
            if nnparts[-termsize:] == termparts:
                del nnparts[-termsize:]
                del nparts[-termsize:]

    if prefix:
        for termsize, termparts in terms:
            if nnparts[:termsize] == termparts:
                del nnparts[:termsize]
                del nparts[:termsize]

    if middle:
        for termsize, termparts in terms:
            if termsize > 1:
                sizediff = nnsize - termsize
                if sizediff > 1 and termparts == ["as.", "oy"]:
                    for i in range(0, nnsize-termsize+1):
                        if termparts == nnparts[i:i+termsize]:
                            del nnparts[i:i+termsize]
                            del nparts[i:i+termsize]
            else:
                if termparts[0] in nnparts[1:-1]:
                    idx = nnparts[1:-1].index(termparts[0])
                    del nnparts[idx+1]
                    del nparts[idx+1]

    return strip_tail(" ".join(nparts))
