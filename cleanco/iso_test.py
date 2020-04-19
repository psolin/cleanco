from termdata_iso3166 import terms_by_country, terms_by_type
from iso3166 import countries

for country_code in terms_by_country:
	try:
		print(country_code)
		print(countries.get(country_code))
		print()
	except:
		print("No country code available.")
		print()