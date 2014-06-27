from cleanco import cleanco

business_name = "Paul, Inc."
test = cleanco(business_name)


print test.cleanname()
print test.country()
print test.type()
print test.industry()


business_name = "A Pharma Company, sa"

test = cleanco(business_name)

print test.cleanname()
print test.country()
print test.type()
print test.industry()