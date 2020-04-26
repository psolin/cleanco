from iso20275 import Elf, ElfEntry

def classifierList():
    property_names=[p for p in dir(ElfEntry) if isinstance(getattr(ElfEntry,p),property)]
    return(property_names)

def allAbbreviations():
    returned_codes = []

    for elf_code, values in Elf.items():
        entity_codes = Elf[elf_code][0].local_abbreviations
        if ";" in entity_codes:
            split = entity_codes.split(';')
            for split_item in split:
                returned_codes.append(split_item)
        else:
            returned_codes.append(entity_codes)
    
    returned_codes = filter(None, returned_codes)
    returned_codes = list(filter(None, returned_codes))

    return(returned_codes)

def idElfCode(abbreviation):
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

    return(ElfCodeList)

def idClassification(code_list,classifier):
    classifier_list = []
    code_list = code_list
    classifier = classifier
    for item in code_list:
    	local_name_list.append(Elf[item][0].classifier)
    # Unique values returned
    myset = set(classifier_list)
    classifier_list = list(myset)
    return(classifier_list)

print(allAbbreviations())