"""Functions to help clean & normalize business names.

See http://www.unicode.org/reports/tr15/#Normalization_Forms_Table for details
on Unicode normalization and the NFKD normalization used here.

Basic usage:

>> terms = get_terms()
>> clean_name("Daddy & Sons, Ltd.", terms)
Daddy & Sons

"""

import functools
import operator
from collections import OrderedDict
import re
import unicodedata
from .termdata import terms_by_type, terms_by_country


tail_removal_rexp = re.compile(r"[^\.\w]+$", flags=re.UNICODE)


def get_terms():
    ts = functools.reduce(operator.iconcat, terms_by_type.values(), [])
    cs = functools.reduce(operator.iconcat, terms_by_country.values(), [])
    return set(ts + cs)

def normalize_terms(terms):
    "retrieve all unique terms from termdata definitions"
    return (unicodedata.normalize("NFKD", t.casefold()) for t in terms)


def strip_tail(name):
    "Get rid of all trailing non-letter symbols except the dot"
    match = re.search(tail_removal_rexp, name)
    if match is not None:
        name = name[: match.span()[0]]
    return name


def normalized(text):
    "caseless Unicode normalization"
    return unicodedata.normalize("NFKD", text.casefold())

"""

def suffix_stripped(name, nname, terms):
    for term, nterm in terms:
        if nname.endswith(' ' + nterm):
            return (name[:-len(term)-1], nname.rstrip(' ' + nterm))
    return (name, nname)

def prefix_stripped(name, nname, terms):
    for term, nterm in terms:
        if nname.startswith(nterm+ ' '):
            return (name[len(term)+1:], nname.lstrip(nterm + ' '))
    return (name, nname)

def inside_removed(name, nname, terms):
    for term, nterm in terms:
        try:
            idx = nname[1:-len(nterm)+1].index(' ' + nterm + ' ')
        except ValueError:
            pass
        else:
            name = name[:idx+2] + name[idx+len(term)+3:]
            nname = nname.replace(' ' + nterm + ' ', ' ')
            return (name, nname)
    return (name, nname)
"""


def splices(s, size):
    "return a list of all in-order string part splices of given size"
    sp = s.split()
    spc = len(sp)
    return [sp[i:i+size] for i in range(0, spc-size+1)]


def basename_partcmp(name, terms, suffix=True, prefix=False, middle=False):
    "expect a list of normalized lists (deconstructed term strings) sorted by size"

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
                if termparts[0] in nnparts:
                    idx = nnparts.index(termparts[0])
                    del nnparts[idx]
                    del nparts[idx]


    return strip_tail(" ".join(nparts))


def basename_partcmp_oneloop(name, terms, suffix=True, prefix=False, middle=False):
    "expect a list of normalized lists (deconstructed term strings) sorted by size"

    name = strip_tail(name)
    nparts = name.split()
    nname = normalized(name)
    nnparts = nname.split()
    nnsize = len(nnparts)

    for termsize, termparts in terms:

        if suffix and nnparts[-termsize:] == termparts:
            del nnparts[-termsize:]
            del nparts[-termsize:]

        if prefix and nnparts[:termsize] == termparts:
            del nnparts[:termsize]
            del nparts[:termsize]

        if middle:
            if termsize > 1:
                sizediff = nnsize - termsize
                if sizediff > 1 and termparts == ["as.", "oy"]:
                    for i in range(0, nnsize-termsize+1):
                        if termparts == nnparts[i:i+termsize]:
                            del nnparts[i:i+termsize]
                            del nparts[i:i+termsize]
            else:
                if termparts[0] in nnparts:
                    idx = nnparts.index(termparts[0])
                    del nnparts[idx]
                    del nparts[idx]

    return strip_tail(" ".join(nparts))


def basename_strcmp(name, terms, suffix=True, prefix=True, middle=False):
    "expect a length-sorted list of normalized term strings"

    # remove any trailing cruft, remove extra whitespace and normalize for comparison
    name = strip_tail(name)
    name = ' '.join(name.split())
    nname = normalized(name)

    # return name without suffixed/prefixed/middle type term(s)

    if suffix:
        for term, nterm in terms:
            if nname.endswith(' ' + nterm):
                name = name[:-len(term)-1]
                nname = nname.rstrip(' ' + nterm)
    if prefix:
        for term, nterm in terms:
            if nname.startswith(nterm+ ' '):
                name = name[len(term)+1:]
                nname = nname.lstrip(nterm + ' ')
    if middle:
        for term, nterm in terms:
            try:
                idx = nname[1:-len(nterm)+1].index(' ' + nterm + ' ')
            except ValueError:
                pass
            else:
                name = name[:idx+2] + name[idx+len(term)+3:]
                nname = nname.replace(' ' + nterm + ' ', ' ')
    return strip_tail(name)


def basename(name, terms, suffix=True, prefix=True, middle=False):
    "use the fastest one"
    return basename_partcmp(name, terms, suffix=True, prefix=True, middle=True)
