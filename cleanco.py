# Note that this script is geared towards identifying businesses in terms of the US/UK

from collections import OrderedDict
import re

from termdata import terms_by_country as country_dict, terms_by_type as type_dict

class cleanco():

	def __init__(self, business_name):

		self.business_name = business_name

		## Abbreviations ##
		self.abbv  = {'intl.':'International', 'intl':'International', 'mfg':'Manufacturing', ' med ':' Medical ', ' ctr':'Center'}

		# Sorted business types / abbreviation by length of business type
		sorted_types = []
		for business_type in type_dict:
			for item in type_dict[business_type]:
				temp_tuple = [business_type, item]
				sorted_types.append(temp_tuple)

		self.sorted_types = sorted(sorted_types, key=lambda part: len(part[1]), reverse=True)

		# Sorted business countries / type abbrviations by length of business type abbreviations
		sorted_countries = []
		for country in country_dict:
			for item in country_dict[country]:
				temp_tuple = [country, item]
				sorted_countries.append(temp_tuple)

		self.sorted_countries = sorted(sorted_countries, key=lambda part: len(part[1]), reverse=True)

		# All of the suffixes sorted by length
		all_sorted = sorted_types + sorted_countries
		suffix_sort = []
		for item in all_sorted:
			suffix_sort.append(item[1])

		self.suffix_sort = sorted(suffix_sort, key=lambda part: len(part), reverse=True)

	def string_stripper(self, business_name):

		# Strip spaces on left and right
		business_name = business_name.strip()

		# Get rid of misc spaces in between
		business_name = " ".join(business_name.split())

		# Get rid of all trailing non-letter symbols
		while re.search(r'\W+$', business_name) is not None:
			business_name = business_name[:-1]

		return business_name

	def end_strip(self, a_set):

		end_set = []

		business_name = self.business_name

		business_name = self.string_stripper(business_name)

		for key, suffix in a_set:
			if ((business_name.lower()).endswith(" " + suffix)):
				end_set.append(key)

		end_set = list(OrderedDict.fromkeys(end_set))

		if end_set != []:
			return end_set
		else:
			return None

	# A clean version of the business name
	def clean_name(self):

		business_name = self.business_name

		# Abbrv. cleanup
		for abbv in self.abbv:
			if abbv in business_name.lower():
				start = (business_name.lower()).find(abbv)
				end = len(business_name)
				business_name = business_name[0:start] + self.abbv[abbv] + business_name[end+1:len(business_name)]

		# Get rid of country items once
		for item in self.suffix_sort:
			if ((business_name.lower()).endswith(" " + item)):
				start = (business_name.lower()).find(item)
				end = len(item)
				business_name = business_name[0:-end]
				business_name = self.string_stripper(business_name)
				break

		business_name = self.string_stripper(business_name)

		return business_name

	def type(self):

		self.type = self.end_strip(self.sorted_types)

		return self.type

	def country(self):

		self.country = self.end_strip(self.sorted_countries)

		return self.country
