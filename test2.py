from cleanco import cleanco

business_name = "Paul, Corp."

x = cleanco(business_name)

print x.clean_name()
print x.type()
print x.country()