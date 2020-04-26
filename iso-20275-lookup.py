from iso20275 import Elf

def allAbbreviations():
    code_list = []

    for elf_code, values in Elf.items():
        entity_codes = Elf[elf_code][0].local_abbreviations
        if ";" in entity_codes:
            split = entity_codes.split(';')
            for split_item in split:
                code_list.append(split_item)
        else:
            code_list.append(entity_codes)
    
    code_list = filter(None, code_list)
    code_list = list(filter(None, code_list))

    return(code_list)

def idElfCode(abbreviation):
    
    ElfCodeList = []
    abbreviation = abbreviation
    
    for elf_code, values in Elf.items():
        entity_codes = Elf[elf_code][0].local_abbreviations
        if ";" in entity_codes:
        	entity_codes = entity_codes.split(';')
        if abbreviation == entity_codes:
        	ElfCodeList.append(elf_code)
        else:
            pass

    return(ElfCodeList)

def idElfLocalName(code_list):
    
    local_name_list = []
    code_list = code_list
    for item in code_list:
    	local_name_list.append(Elf[item][0].local_name)
    return(local_name_list)