from cleanco import cleanco

business_name = "Hello World, ltd."
print
print business_name
x = cleanco(business_name)
print x.clean_name()
print
print x.type()
print x.country()
print