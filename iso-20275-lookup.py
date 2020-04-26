from iso20275 import Elf

def allcodes():
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

print(allcodes())