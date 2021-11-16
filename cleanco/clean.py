"""Functions to help clean & normalize business names.

See http://www.unicode.org/reports/tr15/#Normalization_Forms_Table for details
on Unicode normalization and the NFKD normalization used here.

Basic usage:

>> terms = prepare_default_terms()
>> basename("Daddy & Sons, Ltd.", terms, prefix=True, middle=True, suffix=True)
Daddy & Sons

"""

import functools
import operator
from collections import OrderedDict
import re
import unicodedata
from .termdata import terms_by_type, terms_by_country
from .non_nfkd_map import NON_NFKD_MAP

tail_removal_rexp = re.compile(r"[^\.\w]+$", flags=re.UNICODE)


def get_unique_terms():
    "retrieve all unique terms from termdata definitions"
    ts = functools.reduce(operator.iconcat, terms_by_type.values(), [])
    cs = functools.reduce(operator.iconcat, terms_by_country.values(), [])
    return set(ts + cs)


def remove_accents(t):
    """based on https://stackoverflow.com/a/51230541"""
    nfkd_form = unicodedata.normalize('NFKD', t.casefold())
    return ''.join(
        NON_NFKD_MAP[c]
            if c in NON_NFKD_MAP
        else c
            for part in nfkd_form for c in part
            if unicodedata.category(part) != 'Mn'
        )


def strip_punct(t):
    return t.replace(".", "").replace(",", "").replace("-", "")


def normalize_terms(terms):
    "normalize terms"
    return (strip_punct(remove_accents(t)) for t in terms)


def strip_tail(name):
    "get rid of all trailing non-letter symbols except the dot"
    match = re.search(tail_removal_rexp, name)
    if match is not None:
        name = name[: match.span()[0]]
    return name


def normalized(text):
    "caseless Unicode normalization"
    return remove_accents(text)


def prepare_default_terms():
    "construct an optimized term structure for basename extraction"
    terms = get_unique_terms()
    nterms = normalize_terms(terms)
    ntermparts = (t.split() for t in nterms)
    # make sure that the result is deterministic, sort terms descending by number of tokens, ascending by names
    sntermparts = sorted(ntermparts, key=lambda x: (-len(x), x))
    return [(len(tp), tp) for tp in sntermparts]


def custom_basename(name, terms, suffix=True, prefix=False, middle=False, **kwargs):
    "return cleaned base version of the business name"

    name = strip_tail(name)
    nparts = name.split()
    nname = normalized(name)
    nnparts = list(map(strip_punct, nname.split()))
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
                if sizediff > 1:
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


# convenience for most common use cases that don't parametrize base name extraction
basename = functools.partial(custom_basename, terms=prepare_default_terms())
