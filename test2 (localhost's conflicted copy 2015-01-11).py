from cleanco import cleanco

business_name = "Cleanco mfg ses."
test = cleanco(business_name)

print business_name
print test.clean_name()
print test.country()
print test.type()