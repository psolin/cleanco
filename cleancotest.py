from cleanco import cleanco

companyname = "Conrad Pharmaceuticals plc"
cleanco = cleanco(companyname)

bustype = cleanco.type()
busind = cleanco.industry()
cleanname = cleanco.cleanname()
short = cleanco.shortname()
country = cleanco.country()

print
print("String: %s") % companyname
print
print("Clean Name: %s") % cleanname
print("Short Name: %s") % short
print("Possible Business Types: %s") % bustype
print("Possible Industry: %s") % busind
print("Possible Country: %s") % country
print