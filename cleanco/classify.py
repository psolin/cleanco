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

from iso20275 import Elf, ElfEntry
from .clean import strip_tail, normalized


def classifiers():
    return(ElfEntry.__dict__.keys())


def classification(source):
    classifier_dict = {}

    for elf_code, values in Elf.items():
        source_match = getattr(Elf[elf_code][0], source)
        if source_match:
            entity_codes = [Elf[elf_code][0].local_abbreviations][0].split(";")
            if entity_codes[0]:
                try:
                    classifier_dict[source_match].extend(entity_codes)
                except:
                    classifier_dict[source_match] = entity_codes
    return(classifier_dict)


def matches(name, source):

    name = strip_tail(name)
    parts = name.split()
    nparts = [normalized(p) for p in parts]
    matches = []

    classified = classification(source)

    for item in classified:
        nitems = [normalized(p) for p in classified[item]]
        if len(set(nparts).intersection(nitems)) > 0:
            matches.append(item)
    return(matches)
