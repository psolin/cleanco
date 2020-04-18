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
from .clean import strip_tail, normalized


def typesources():
   "business types / abbreviations sorted by length of business type"
   types = []
   for business_type in terms_by_type:
       for item in terms_by_type[business_type]:
           types.append((business_type, item))

   return sorted(types, key=lambda part: len(part[1]), reverse=True)


def countrysources():
   "business countries / type abbreviations sorted by length of type abbreviations"
   countries = []
   for country in terms_by_country:
       for item in terms_by_country[country]:
           countries.append((country, item))

   return sorted(countries, key=lambda part: len(part[1]), reverse=True)


def matches(name, sources):
    "get types or countries matching with the legal terms in name"

    name = strip_tail(name)
    parts = name.split()
    nparts = [normalized(p) for p in parts]
    matches = []
    for classifier, term in sources:
        nterm = normalized(term)
        try:
            idx = nparts.index(nterm)
        except ValueError:
            pass
        else:
            matches.append(classifier)

    return matches

