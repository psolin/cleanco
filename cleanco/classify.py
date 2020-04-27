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
    property_names = [p for p in dir(ElfEntry) if isinstance(
        getattr(ElfEntry, p), property)]
    return(property_names)


def classification(abbreviation, source):
    classifier_list = []
    ElfCodeList = []
    abbreviation = abbreviation

    for elf_code, values in Elf.items():
        entity_codes = Elf[elf_code][0].local_abbreviations
        if ";" in entity_codes:
            entity_codes = entity_codes.split(';')
        if abbreviation in entity_codes:
            ElfCodeList.append(elf_code)
        else:
            pass

    for item in ElfCodeList:
        test = getattr(Elf[item][0], source)
        classifier_list.append(test)
    # Unique values returned
    myset = set(classifier_list)
    classifier_list = list(myset)
    return(classifier_list)


def matches(name, source):

    name = strip_tail(name)
    parts = name.split()
    nparts = [normalized(p) for p in parts]
    match_list = []
    matches = []

    for term in nparts:
        try:
            nterm = normalized(term)
            classification_list = classification(nterm, source)
            match_list.append(classification_list)
        except ValueError:
            pass

    try:
        for item in classification_list:
            matches.append(item)
    except:
        pass

    return matches
