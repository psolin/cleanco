# Note that this script is geared towards identifying businesses in terms of the US/UK

from collections import OrderedDict
import re

from termdata import terms_by_country as country_dict, terms_by_type as type_dict


# Sorted business types / abbreviation by length of business type
sorted_types = []
for business_type in type_dict:
	for item in type_dict[business_type]:
		temp_tuple = [business_type, item]
		sorted_types.append(temp_tuple)
sorted_types = sorted(sorted_types, key=lambda part: len(part[1]), reverse=True)

# Sorted business countries / type abbrviations by length of business type abbreviations
sorted_countries = []
for country in country_dict:
	for item in country_dict[country]:
		temp_tuple = [country, item]
		sorted_countries.append(temp_tuple)
sorted_countries = sorted(sorted_countries, key=lambda part: len(part[1]), reverse=True)

# All of the suffixes sorted by length
all_sorted = sorted_types + sorted_countries
suffix_sort = []
for item in all_sorted:
	suffix_sort.append(item[1])
suffix_sort = sorted(suffix_sort, key=lambda part: len(part), reverse=True)


class cleanco(object):

	def __init__(self, business_name):
		# always do non-visible cleanup, but store the original just in case
		self.business_name = ' '.join(business_name.split())
		self._original = business_name

	def string_stripper(self, business_name):

		# Get rid of extra prefix-, suffix- & in-between spaces
		business_name = " ".join(business_name.split())

		# Get rid of all trailing non-letter symbols
		while re.search(r'\W+$', business_name, flags=re.UNICODE) is not None:
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


	def clean_name(self, suffix=True, prefix=False, middle=False, multi=False):
		"return cleared version of the business name"

		name = self.business_name

		# return name without suffixed/prefixed/middle type term(s)

		for item in suffix_sort:
			if suffix:
				if name.lower().endswith(" " + item):
					start = name.lower().find(item)
					end = len(item)
					name = name[0:-end-1]
					name = self.string_stripper(name)
					if multi==False:
						break
			if prefix:
				if name.lower().startswith(item+' '):
					name = name[len(item)+1:]
					if multi==False:
						break
			if middle:
				term = ' ' + item + ' '
				if term in name.lower():
					start = name.lower().find(term)
					end = start + len(term)
					name = name[:start] + " " + name[end:]
					if multi==False:
						break

		return self.string_stripper(name)


	def type(self):
		self.type = self.end_strip(sorted_types)
		return self.type

	def country(self):
		self.country = self.end_strip(sorted_countries)
		return self.country
