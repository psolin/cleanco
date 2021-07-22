import unicodedata
from .non_nfkd_map import NON_NFKD_MAP
import re

tail_removal_rexp = re.compile(r"[^\.\w]+$", flags=re.UNICODE)


def remove_accents(t):
    """based on https://stackoverflow.com/a/51230541"""
    nfkd_form = unicodedata.normalize("NFKD", t.casefold())
    return "".join(
        NON_NFKD_MAP[c] if c in NON_NFKD_MAP else c
        for part in nfkd_form
        for c in part
        if unicodedata.category(part) != "Mn"
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

def find_sublist(mylist, pattern):
    """
    Inspired by https://stackoverflow.com/questions/10106901/elegant-find-sub-list-in-list
    """
    assert len(pattern) > 0 and len(mylist) > 0
    if len(pattern) > len(mylist):
        return False

    matches = []
    for i in range(len(mylist)-len(pattern)+1):
        if mylist[i] == pattern[0] and mylist[i:i+len(pattern)] == pattern:
            #matches.append(pattern)
            return True
    return False
