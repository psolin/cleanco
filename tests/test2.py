from cleanco import cleanco

business_name = "Hello World, llc."
print("Inputted Business Name: %s" % business_name)
x = cleanco(business_name)
print("Clean Name: %s" % x.clean_name())
print("Business Type: %s" % x.type())
print("Country: %s" % x.country())