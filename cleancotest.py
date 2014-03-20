from cleanco import cleanco

business_name = "Merck Pharmaceutials - Corporate (formerly Not Merck) LLC"

processing = cleanco(business_name)
x = processing.cleaner()

print
print business_name
print
print("Clean Name: %s") % (x.clean_name)
print("Possible Industries: %s") % (x.industry)
print("Possible Business Types: %s") % (x.type)
print("Possible Countries: %s") % (x.country)
print