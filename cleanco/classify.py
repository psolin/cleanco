"""
Functions to help classify business names by country or type, based on legal terms.

Examples of use:

# check name for its possible business type(s)
>> matches("MyCompany Ltd", "local_name")
['Private Limited by Guarantee', 'Private Limited Company', 'Limited Liability Company', 'New Generation Co-operatives']

# check name for its possible countries
>> matches("MyCompany Ltd", "country")
['United States of America', 'United Kingdom', 'Canada']

"""

from .iso20275lookup import idClassification
from .clean import strip_tail, normalized

def matches(name, source):

    name = strip_tail(name)
    parts = name.split()
    nparts = [normalized(p) for p in parts]
    match_list = []
    matches = []

    for term in nparts:
        try:
            nterm = normalized(term)
            classification_list = idClassification(nterm,source)
            match_list.append(classification_list)
        except ValueError:
          pass

    try:
        for item in classification_list:
            matches.append(item)
    except:
      pass


    return matches