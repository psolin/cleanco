"""
Functions to help classify business names by country or type, based on legal terms.

Examples of use:

>> # check name for its possible business type(s)
>> classification_sources = typesources()
>> matches("MyCompany Ltd", classification_sources)
['Limited']
>>

>> # check name for its possible jurisdictions, usually countries
>> classification_sources = countrysources()
>> matches("MyCompany Ltd", classification_sources)
['New Zealand', 'United Kingdom', 'United States of America']
>>

"""

from .termdata import terms_by_country, terms_by_type
from .utils import strip_punct, strip_tail, normalized, normalize_terms, find_sublist


def typesources():
    "business types / abbreviations sorted by length of business type"
    types = []
    for business_type, type_terms in terms_by_type.items():
        for item in set(normalize_terms(type_terms)):
            types.append((business_type, item.split()))

    return sorted(types, key=lambda part: len(part[1]), reverse=True)


def countrysources():
    "business countries / type abbreviations sorted by length of type abbreviations"
    countries = []
    for country, country_terms in terms_by_country.items():
        for item in set(normalize_terms(country_terms)):
            countries.append((country, item.split()))

    return sorted(countries, key=lambda part: len(part[1]), reverse=True)


def matches(name, sources):
    "get types or countries matching with the legal terms in name"
    name = strip_tail(name)
    nname = normalized(name)
    nnparts = list(map(strip_punct, nname.split()))

    matches = []
    for classifier, term in sources:
        if find_sublist(nnparts, term):
            matches.append((classifier, term))

    # sort by length of matched tokens
    matches = sorted(matches, key=lambda x: -len(x[1]))
    disamb_matches = []

    # removing matches that are part of a longer better match
    for classifier, term in matches:
        # if there is a term in disamb_matches that already
        # contains the new term skip it, otherwise add
        if not any(
            len(term_other) > len(term) and find_sublist(term_other, term)
            for _, term_other in disamb_matches
        ):
            disamb_matches.append((classifier, term))

    return [class_ for class_, _ in disamb_matches]
