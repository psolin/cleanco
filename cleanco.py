# Note that this script is geard towards identifying businesses in terms of the US/UK
from collections import OrderedDict
class cleanco():
	
	def __init__(self, business_name):
		
		self.business_name = business_name

		# Business Types
		type_dict = {}
		type_dict['Professional Limited Liability Company'] = ["pllc", "p.l.l.c."]
		type_dict['Limited Liability Limited Partnership'] = ["lllp", "l.l.l.p."]
		type_dict['Limited Partnership'] = ["gmbh & co. kg", "gmbh & co. kg", "lp", "l.p.", "s.c.s.", "s.c.p.a", "comm.v", "k.d.", "k.d.a.", "s. en c.", "e.e.", "s.a.s.", "s. en c.", "c.v.", "s.k.a.", "sp.k.", "s.cra.", "ky", "scs", "kg", "kd", "k/s", "ee", "secs", "kda", "ks", "kb", "kt"]
		type_dict['Corporation'] = ["company", "incorporated", "corporation", "corp", "inc", "& co.", "& co", "inc.", "s.p.a.", "n.v.", "a.g.", "ag", "nuf", "s.a.", "s.f.", "oao", "co."]
		type_dict['General Partnership'] = ["soc.col.", "stg", "d.n.o.", "ltda.", "v.o.s.", "kgaa", "o.e.", "s.f.", "s.n.c.", "s.a.p.a.", "j.t.d.", "v.o.f.", "sp.j.", "og", "sd", "vos", " i/s", "ay", "snc", "oe", "bt.", "s.s.", "mb", "ans", "da", "o.d.", "hb", "pt"]
		type_dict['Limited Liability Company'] = ["pllc", "llc", "l.l.c.", "plc.", "plc", "hf.", "oyj", "a.e.", "nyrt.", "p.l.c.", "sh.a.", "s.a.", "s.r.l.", "srl.", "aat", "3at", "d.d.", "akc. spol.", "a.s.", "s.r.o.", "s.m.b.a.", "smba", "sarl", "nv", "sa", "aps", "a/s", "p/s", "sae", "sasu", "eurl", "ae", "cpt", "as", "ab", "asa", "ooo", "dat", "vat", "zat", "mchj", "a.d."]
		type_dict['Limited Liability Partnership'] = ["llp", "l.l.p.", "sp.p.", "s.c.a.", "s.c.s."]
		type_dict['Limited'] = ["pty. ltd.", "pty ltd", "ltd", "l.t.d.", "bvba", "d.o.o.", "ltda", "gmbh", "g.m.b.h", "kft.", "kht.", "zrt.", "ehf.", "s.a.r.l.", "d.o.o.e.l.", "s. de r.l.", "b.v.", "tapui", "sp. z.o.o.", "s.r.l.", "s.l.", "s.l.n.e.", "ood", "oy", "rt.", "teo", "uab", "scs", "sprl", "limited", "bhd.", "sdn. bhd.", "sdn bhd", "as", "lda.", "tov", "pp"]
		type_dict['Professional Corporation'] = ["p.c.", "vof", "snc"]
		type_dict['No Liability'] = ["nl"]
		type_dict['Sole Proprietorship'] = ["e.u.", "s.p.", "t:mi", "e.v.", "e.c.", "et", "obrt", "fie", "ij", "fop", "xt"]
		type_dict['Joint Stock / Unlimited'] = ["unltd", "ultd", "sal", "unlimited", "saog", "saoc", "aj", "yoaj", "oaj"]
		type_dict['Joint Venture'] = ["esv", "gie", "kv.", "qk"]
		type_dict['Non-Profit'] = ["vzw", "ses.", "gte."]
		type_dict['Mutual Fund'] = ["sicav"]
		type_dict['Private Company'] = ["private", "pte", "xk"]

		# Countries that can be identified due to specific business types in the name -- thanks Wikipedia!
		country_dict = {}
		country_dict['Albania'] = ["sh.a.", "sh.p.k."]
		country_dict['Argentina'] = ["s.a.", "s.r.l.", "s.c.p.a", "scpa", "s.c.e i.", "s.e.", "s.g.r", "soc.col."]
		country_dict['Australia'] = ["nl", "pty. ltd.", "pty ltd"]
		country_dict['Austria'] = ["e.u.", "stg", "gesbr", "a.g.", "ag", "og", "kg"]
		country_dict['Belarus'] = ["aat", "3at"]
		country_dict['Belgium'] = ["esv", "vzw", "vof", "snc", "comm.v", "scs", "bvba", "sprl", "cbva", "cvoa", "sca", "sep", "gie"]
		country_dict['Bosnia / Herzegovina'] = ["d.d.", "a.d.", "d.n.o.", "d.o.o.", "k.v.", "s.p."]
		country_dict['Bulgaria'] = ["ad", "adsitz", "ead", "et", "kd", "kda", "sd"]
		country_dict['Brazil'] = ["ltda", "s.a.", "pllc", "ad", "adsitz", "ead", "et", "kd", "kda", "sd"]
		country_dict['Cambodia'] = ["gp", "sm pte ltd.", "pte ltd.", "plc ltd.", "peec", "sp"]
		country_dict['Canada'] = ["gp", "lp", "sp"]
		country_dict['Chile'] = ["eirl", "s.a.", "sgr", "s.g.r.", "ltda", "s.p.a.", "sa", "s. en c.", "ltda."]
		country_dict['Columbia'] = ["s.a.", "e.u.", "s.a.s.", "suc. de descendants", "sca"]
		country_dict['Croatia'] = ["d.d.", "d.d.o.", "obrt"]
		country_dict['Czech Republic'] = ["a.s.", "akc. spol.", "s.r.o.", "v.o.s.", "k.s.", "sro", "vos"]
		country_dict['Denmark'] = ["i/s", "a/s", "k/s", "p/s", "amba", "a.m.b.a.", "fmba", "f.m.b.a.", "smba", "s.m.b.a.", "g/s"]
		country_dict['Dominican Republic'] = ["c. por a.", "cxa", "s.a.", "s.a.s.", "srl.", "eirl.", "sa", "sas"]
		country_dict['Ecuador'] = ["s.a.", "c.a.", "sa", "ep"]
		country_dict['Egypt'] = ["sae"]
		country_dict['Estonia'] = ["fie"]
		country_dict['Finland'] = ["t:mi", "ay", "ky", "oy", "oyj", "ok"]
		country_dict['France'] = ["sicav", "sarl", "sogepa", "ei", "eurl", "sasu", "fcp", "gie", "sep", "snc", "scs", "sca", "scop", "sem", "sas"]
		country_dict['Germany'] = ["gmbh & co. kg", "gmbh & co. kg", "e.g.", "e.v.", "gbr", "ohg", "partg", "kgaa", "gmbh", "g.m.b.h.", "ag"]
		country_dict['Greece'] = ["a.e.", "ae", "e.e.", "ee", "epe", "e.p.e.", "mepe", "m.e.p.e.", "o.e.", "oe", "ovee", "o.v.e.e."]
		country_dict['Guatemala'] = ["s.a.", "sa"]
		country_dict['Haiti'] = ["sa"]
		country_dict['Hong Kong'] = ["ltd", "unltd", "ultd"]
		country_dict['Hungary'] = ["e.v.", "e.c.", "bt.", "kft.", "kht.", "kkt.", "k.v.", "zrt.", "nyrt", "ev", "ec", "rt."]
		country_dict['Iceland'] = ["ehf.", "hf.", "ohf.", "s.f.", "ses."]
		country_dict['India'] = ["pvt. ltd.", "ltd.", "psu", "pse"]
		country_dict['Indonesia'] = ["ud", "fa", "pt"]
		country_dict['Ireland'] = ["cpt", "teo"]
		country_dict['Israel'] = ["b.m.", "bm", "ltd"]
		country_dict['Italy'] = ["s.n.c.", "s.a.s.", "s.p.a.", "s.a.p.a.", "s.r.l.", "s.c.r.l.", "s.s."]
		country_dict['Latvia'] = ["as", "sia", "ik", "ps", "ks"]
		country_dict['Lebanon'] = ["sal"]
		country_dict['Lithuania'] = ["uab", "ab", "ij", "mb"]
		country_dict['Luxemborg'] = ["s.a.", "s.a.r.l.", "secs"]
		country_dict['Macedonia'] = ["d.o.o.", "d.o.o.e.l", "k.d.a.", "j.t.d.", "a.d.", "k.d."]
		country_dict['Malaysia'] = ["bhd.", "sdn. bhd."]
		country_dict['Mexico'] = ["s.a.", "s. de. r.l.", "s. en c.", "s.a.b.", "s.a.p.i."]
		country_dict['Mongolia'] = ["xk", "xxk"]
		country_dict['Netherlands'] = ["v.o.f.", "c.v.", "b.v.", "n.v."]
		country_dict['New Zealand'] = ["tapui", "ltd"]
		country_dict['Nigeria'] = ["gte.", "plc", "ltd.", "ultd."]
		country_dict['Norway'] = ["asa", "as", "ans", "ba", "bl", "da", "etat", "fkf", "hf", "iks", "kf", "ks", "nuf", "rhf", "sf"]
		country_dict['Oman'] = ["saog", "saoc"]
		country_dict['Pakistan'] = ["ltd.", "pvt. ltd.", "ltd"]
		country_dict['Peru'] = ["sa", "s.a.", "s.a.a."]
		country_dict['Philippines'] = ["coop.", "corp.", "corp", "ent.", "inc.", "inc", "llc", "l.l.c.", "ltd."]
		country_dict['Poland'] = ["p.p.", "s.k.a.", "sp.j.", "sp.k.", "sp.p.", "sp. z.o.o.", "s.c.", "s.a."]
		country_dict['Portugal'] = ["lda.", "crl", "s.a.", "s.f.", "sgps"]
		country_dict['Romania'] = ["s.c.a.", "s.c.s.", "s.n.c.", "s.r.l.", "o.n.g.", "s.a."]
		country_dict['Russia'] = ["ooo", "oao", "zao", "3ao"]
		country_dict['Serbia'] = ["d.o.o.", "a.d.", "k.d.", "o.d."]
		country_dict['Singapore'] = ["bhd", "pte ltd", "sdn bhd", "llp", "l.l.p.", "ltd.", "pte"]
		country_dict['Slovokia'] = ["a.s.", "s.r.o.", "k.s.", "v.o.s."]
		country_dict['Slovenia'] = ["d.d.", "d.o.o.", "d.n.o.", "k.d.", "s.p."]
		country_dict['Spain'] = ["s.a.", "s.a.d.", "s.l.", "s.l.l.", "s.l.n.e.", "s.c.", "s.cra", "s.coop", "sal", "sccl"]
		country_dict['Sweden'] = ["ab", "hb", "kb"]
		country_dict['Switzerland'] = ["ab", "sa", "gmbh", "g.m.b.h.", "sarl", "sagl"]
		country_dict['Turkey'] = ["koop."]
		country_dict['Ukraine'] = ["dat", "fop", "kt", "pt", "tdv", "tov", "pp", "vat", "zat", "at"]
		country_dict['United Kingdon'] = ["plc.", "plc", "uk", "cic", "cio", "l.l.p.", "llp", "l.p.", "lp", "ltd.", "ltd"]
		country_dict['United States of America'] = ["llc", "inc.", "corporation", "incorporated", "company", "limited", "corp.", "inc.", "inc", "llp", "l.l.p.", "pllc", "and company", "& company", "usa", "inc", "inc.", "corp.", "corp", "ltd.", "ltd", "& co.", "& co", "co.", "co", "lp", "us"]
		country_dict['Uzbekistan'] = ["mchj", "qmj", "aj", "oaj", "yoaj", "xk", "xt", "ok", "uk", "qk"]

		## Abbreviations ##
		self.abbv  = {'intl.':'International', 'intl':'International', 'co.':'Company', 'mfg':'Manufacturing', ' med ':' Medical ', 'ctr':'Center'}

		# Abbreviations when strings end with these
		self.abbvend = {' co':'Company'}

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
		
		# Get rid of everything in parenthesis
		if " (" and ")" in business_name:
			beginpar = business_name.find(" (")
			endpar = business_name.find(")")
			business_name = business_name.replace(business_name[beginpar:endpar+1],"")

		# Strip out commas
		if "," in business_name:
			business_name = business_name.replace(",", " ")

		# Strip spaces on the left
		business_name = business_name.lstrip()

		#Strip spaces on the right
		business_name = business_name.strip()

		# Get rid of misc spaces in between
		business_name = " ".join(business_name.split())

		return business_name

	def end_strip(self, a_set):

		end_set = []

		business_name = self.business_name

		business_name = self.string_stripper(business_name)

		for key, suffix in a_set:
			suffix = " " + suffix
			if ((business_name.lower()).endswith(suffix)):
				end_set.append(key)

		end_set = list(OrderedDict.fromkeys(end_set))

		if end_set != []:
			return end_set
		else:
			return None

	# A clean version of the business name
	def clean_name(self):

		business_name = self.business_name

		# Get rid of everything in parenthesis
		if " (" and ")" in business_name:
			beginpar = business_name.find(" (")
			endpar = business_name.find(")")
			business_name = business_name.replace(business_name[beginpar:endpar+1],"")

		# Get rid of everything after hyphen and spaces
		if " - " in business_name:
			corplen = len(business_name)
			hypenloc = business_name.find(" - ")
			business_name = business_name.replace(business_name[hypenloc:corplen],"")

		# Abbrv. cleanup
		for abbv in self.abbv:
			if abbv in business_name.lower():
				start = (business_name.lower()).find(abbv)
				end = len(business_name)
				business_name = business_name[0:start] + self.abbv[abbv] + business_name[end+1:len(business_name)]

		# Replace single hyphen with space
		if "-" in business_name:
			corplen = len(business_name)
			hypenloc = business_name.find("-")
			business_name = business_name.replace("-"," ")

		# Get rid of country items:
		for item in self.suffix_sort:
			if ((business_name.lower()).endswith(item)):
				start = (business_name.lower()).find(item)
				end = len(item)
				end = end * -1
				business_name = business_name[0:end]
				business_name = self.string_stripper(business_name)

		business_name = self.string_stripper(business_name)

		return business_name

	def type(self):
		
		self.type = self.end_strip(self.sorted_types)

		return self.type

	def country(self):

		self.country = self.end_strip(self.sorted_countries)

		return self.country