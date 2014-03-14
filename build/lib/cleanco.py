# Note that this script is geard towards identifying businesses in terms of the US/UK
from collections import OrderedDict

class cleanco():
	
	def __init__(self, corpname):
		
		# Throw this in there so that I know it's there
		self.corpname = corpname

		## Business Type ##

		#Weird US ones
		# Professional Limited Liability Company - PLLC
		self.pllc = ["pllc", "p.l.l.c."]

		# Limited Liability Limited Partnership
		self.lllp = ["lllp", "l.l.l.p."]

		# Corporation
		self.corp = ["incorporated", "corporation", "corp", " inc", " & co.", "inc.", "s.p.a.", "n.v."]
		# Corporations when string end with these
		self.corp_end = [" a.g.", " ag", " nuf", " s.a.", " s.f.", " oao"]

		# GP - General Partnership
		self.gp = ["soc.col.", "stg", "d.n.o.", "ltda.", "v.o.s.", "kgaa", "o.e.", "s.f.", "s.n.c.", "s.a.p.a.", "j.t.d.", "v.o.f.", "sp.j."]
		self.gp_end = [" og", " sd", " vos", " i/s", " ay", " snc", " oe", " bt.", " s.s.", " mb", " ans", " da", " o.d.", " hb", "pt"]

		# LLC - Limited Liability Company (PLC - UK)
		self.llc = ["pllc", "llc", "l.l.c.", "plc", "hf.", "oyj", "a.e.", "nyrt.", "p.l.c.", "sh.a.", "s.a.", "s.r.l.", "srl.", "aat", "3at", "d.d.", "akc. spol.", "a.s.", "s.r.o.", "s.m.b.a.", "smba", "sarl"]
		self.llc_end = [" nv", " sa", " aps", " a/s", " p/s", " sae", " sasu", "eurl", " ae", " cpt", " as", " ab", " asa", " ooo", " dat", " vat", " zat", " mchj", " a.d."]
		
		# LLP - Limited Liability Partnership
		self.llp = ["llp", "l.l.p.", "sp.p.", "s.c.a.", "s.c.s."]
		
		# LP - Limited Partnership
		self.lp = [" lp", "l.p.", "s.c.s.", "s.c.p.a", "comm.v", "k.d.", "k.d.a.", "s. en c.", "e.e.", "s.a.s.", "s. en c.", "c.v.", "s.k.a.", "sp.k.", "s.cra."]
		self.lp_end = [" ky", " scs", " kg", " kd", " k/s", " ee", " secs", " kda", " ks", " kb", " kt"]

		# Ltd - Private Company Limited By Shares - UK
		self.ltd = ["pty. ltd.", "pty ltd", "ltd", "l.t.d.", "bvba", "d.o.o.", "ltda", "gmbh", "g.m.b.h", "kft.", "kht.", "zrt.", "ehf.", "s.a.r.l.", "d.o.o.e.l.", "s. de r.l.", "b.v.", "tapui", "sp. z.o.o.", "s.r.l.", "s.l.", "s.l.n.e."]
		self.ltd_end = [" ood", " oy", " rt.", " teo", " uab", " scs", " sprl", " limited", " bhd.", " sdn. bhd.", " sdn bhd", " as", " lda.", " tov", " pp"]
		
		# PC - Professional Corporation -- contains a comma
		self.pc_comma = ["p.c.", ", pc", "vof", "snc"]

		# NL - No Liability - Australia
		self.nl_end = [" nl"]

		# SP - Sole Proprietorship
		self.sp = ["e.u.", "s.p.", "t:mi", "e.v.", "e.c."]
		self.sp_end = [" et", " obrt", " fie", " ij", " fop", " xt"]

		# Joint Stock - Unlimited
		self.js = ["unltd", "ultd"]
		self.js_end = [" sal", "unlimited", " saog", " saoc", " aj", " yoaj", " oaj"]

		# Joint Venture
		self.jv_end = [" esv", " gie", " kv.", " qk"]

		# Non-Profit
		self.np = ["vzw", "ses.", "gte."]

		# Mutual Fund
		self.mf = ["sicav"]

		# Countries that can be identified due to specific business types in the name -- thanks Wikipedia!
		self.albania = ["sh.a.", "sh.p.k."]
		self.argentina = ["s.a.", "s.r.l.", "s.c.p.a", " scpa", "s.c.e i.", "s.e.", "s.g.r", "soc.col."]
		self.australia = [" nl", "pty. ltd.", "pty ltd"]
		self.austria = ["e.u.", "stg", "gesbr", "a.g."]
		self.austria_end = [" ag", " og", " kg"]
		self.belarus = ["aat", "3at"]
		self.belgium = ["esv", "vzw", "vof", "snc", "comm.v", "scs", "bvba", "sprl", "cbva", "cvoa"]
		self.belgium_end = [" sca", " sep", " gie"]
		self.bosherz = ["d.d.", " a.d.", "d.n.o.", "d.o.o.", "k.v.", "s.p."]
		self.brazil = ["ltda", "s.a.", "pllc"]
		self.bulgaria_end = [" ad", "adsitz", " ead", " et", "kd", "kda", " sd"]
		self.cambodia = ["gp", "sm pte ltd.", "pte ltd.", "plc ltd.", "peec"]
		self.cambodia_end = [" sp"]
		self.canada = ["gp", " lp"]
		self.canada_end = [" sp"]
		self.chile = ["eirl", "s.a.", "sgr", "s.g.r.", "ltda", "s.p.a."]
		self.chile_end = [" sa", "s. en c.", "ltda."]
		self.columbia = ["s.a.", "e.u.", "s.a.s.", "suc. de descendants"]
		self.columbia_end = [" sca"]
		self.croatia = ["d.d.", "d.d.o."]
		self.croatia_end = [" obrt"]
		self.czech = ["a.s.", "akc. spol.", "s.r.o.", "v.o.s.", "k.s."]
		self.czech_end = [" sro", " vos"]
		self.denmark = [" i/s", " a/s", " k/s", " p/s", "amba", "a.m.b.a.", "fmba", "f.m.b.a.", "smba", "s.m.b.a.", " g/s"]
		self.domrep = [" c. por a.", "cxa", "s.a.", "s.a.s.", "srl.", "eirl."]
		self.domrep_end = [" sa", " sas"]
		self.ecuador = ["s.a.", "c.a."]
		self.ecuador_end = [" sa", " ep"]
		self.egypt_end = [" sae"]
		self.estonia_end = [" fie"]
		self.finland = ["t:mi"]
		self.finland_end = [" ay", " ky", " oy", " oyj", " ok"]
		self.france = ["sicav", "sarl", "sogepa"]
		self.france_end = [" ei", " eurl", " sasu", " fcp", " gie", " sep", " snc", " scs", " sca", " scop", " sem", " sas"]
		self.germany = ["e.g.", "e.v.", "gbr", "ohg", "partg", "kgaa", "gmbh", "g.m.b.h."]
		self.germany_end = [" ag"]
		self.greece_end = [" a.e.", " ae", "e.e.", " ee", " epe", "e.p.e.", " mepe", "m.e.p.e.", "o.e.", " oe", " ovee", "o.v.e.e."]
		self.guatemala_end = [" s.a.", " sa"]
		self.haiti_end = [" sa"]
		self.hongkong = ["ltd", "unltd", "ultd"]
		self.hungary = ["e.v.", "e.c.", "bt.", "kft.", "kht.", "kkt.", "k.v.", "zrt.", "nyrt"]
		self.hungary_end = [" ev", " ec", " rt."]
		self.iceland = ["ehf.", "hf.", "ohf.", "s.f.", "ses."]
		self.india = ["pvt. ltd.", "ltd."]
		self.india_end = [" psu", " pse"]
		self.indonesia_end = [" ud", " fa", " pt"]
		self.ireland_end = [" cpt", " teo"]
		self.israel_end = [" b.m.", " bm", " ltd"]
		self.italy = ["s.n.c.", "s.a.s.", "s.p.a.", "s.a.p.a.", "s.r.l.", "s.c.r.l."]
		self.italy_end = [" s.s."]
		self.latvia_end = [" as", " sia", " ik", " ps", " ks"]
		self.lebanon_end = [" sal"]
		self.lithuania_end = [" uab", " ab", " ij", " mb"]
		self.luxemborg = ["s.a.", "s.a.r.l."]
		self.luxemborg_end = [" secs"]
		self.macedonia = ["d.o.o.", "d.o.o.e.l", "k.d.a.", "j.t.d."]
		self.macedonia_end = [" a.d.", " k.d."]
		self.malaysia_end = [" bhd.", "sdn. bhd."]
		self.mexico = ["s.a.", "s. de. r.l.", "s. en c.", "s.a.b.", "s.a.p.i."]
		self.mongolia_end = [" xk", " xxk"]
		self.netherlands = ["v.o.f.", "c.v.", "b.v.", "n.v."]
		self.newzealand = ["tapui"]
		self.newzealand_end = [" ltd"]
		self.nigeria = ["gte.", "plc"]
		self.nigeria_end = [" ltd.", "ultd."]
		self.norway_end = [" asa", " as", " ans", " ba", " bl", " da", " etat", "fkf", " hf", " iks", " kf", " ks", " nuf", " rhf", " sf"]
		self.oman_end = ["saog", "saoc"]
		self.pakistan = ["ltd.", "pvt. ltd."]
		self.pakistan_end = [" ltd"]
		self.peru_end = [" sa", " s.a.", " s.a.a."]
		self.philippines_end = [" coop.", " corp.", " corp", " ent.", " inc.", " inc", " llc", " l.l.c.", " ltd."]
		self.poland = ["p.p.", "s.k.a.", "sp.j.", "sp.k.", "sp.p.", "sp. z.o.o."]
		self.poland_end = [" s.c.", " s.a."]
		self.portugal = ["lda."]
		self.portugal_end = [" crl", " s.a.", " s.f.", " sgps"]
		self.romania = ["s.c.a.", "s.c.s.", "s.n.c.", "s.r.l.", "o.n.g."]
		self.romania_end = [" s.a."]
		self.russia_end = [" ooo", " oao", " zao", " 3ao"]
		self.serbia = ["d.o.o.", ]
		self.serbia_end = [" a.d.", " k.d.", " o.d."]
		self.singapore = ["bhd", "pte ltd", "sdn bhd"]
		self.singapore_end = ["llp", " l.l.p.", " ltd.", "pte"]
		self.slovokia_end = [" a.s.", " s.r.o.", " k.s.", " v.o.s."]
		self.slovenia_end = [" d.d.", " d.o.o.", " d.n.o.", " k.d.", " s.p."]
		self.spain_end = [" s.a.", " s.a.d.", " s.l.", " s.l.l.", " s.l.n.e.", " s.c.", " s.cra", " s.coop", " sal", " sccl"]
		self.sweden_end = [" ab", " hb", " kb"]
		self.switzerland_end = [" ab", " sa", " gmbh", " g.m.b.h.", " sarl", " sagl"]
		self.turkey = [" koop."]
		self.ukraine_end = [" dat", " fop", " kt", " pt", " tdv", " tov", " pp", " vat", " zat", " at"]
		self.uk = ["plc"]
		self.uk_end = [" uk", " cic", " cio", " l.l.p.", " llp", " l.p.", " lp", " ltd.", " ltd"]
		self.usa = [" inc.", "corporation", "incorporated" "company", "limited", "corp.", "inc.", "inc", "llp", "l.l.p.", "pllc", " and company", " & company"]
		self.usa_end = [" usa", " inc", " inc.", " corp.", " corp", " ltd.", "ltd", " & co."," co.", " co", " lp"]
		self.uzbekistan_end = [" mchj", " qmj", " aj", " oaj", " yoaj", " xk", " xt", " ok" " uk", " qk"]

		# Private company?
		self.pte = ["private"]
		self.pte_end = ["pte", " xk"]

		
		## Abbreviations ##
		self.abbv  = {'intl':'International', 'co.':'Company', 'mfg':'Manufacturing'}

		# Abbreviations when strings end with these
		self.abbvend = {' co':'Company'}


		## Industry ##
		self.busind = ["Pharmaceutical, Biotechnology", "Engineering"]
		self.pharma = [" therap", "biopharmaceuticals", "biopharmaceutical", "biopharma", "biopharm", "pharmaceuticals", "pharmaceutical", "pharma"]
		self.biotech = [" therap", "biopharmaceuticals", "biopharmaceutical", "biopharma", "biopharm", "biotechnology", "biotechnologies", "bioventures", "biolabs", "biosciences", "bioscience", "biotech"]
		self.engineering = ["engineer"]
		self.education = ["education", "university", "school of", "academy"]

	def masterlist(self):
		mlist = self.albania + self.argentina + self.australia + self.austria + self.belarus + self.belgium + self.bosherz + self.brazil + self.cambodia + self.canada + self.chile + self.columbia + self.croatia + self.czech + self.denmark + self.domrep + self.ecuador + self.finland + self.france + self.germany + self.hongkong + self.hungary + self.iceland + self.india + self.italy + self.luxemborg +  self.macedonia + self.mexico + self.netherlands + self.newzealand + self.nigeria + self.pakistan + self.peru_end + self.poland + self.portugal + self.romania + self.serbia + self.singapore + self.turkey + self.uk + self.usa
		return list(OrderedDict.fromkeys(mlist))

	def masterlist_end(self):
		mlist =	self.austria_end + self.belgium_end + self.bulgaria_end + self.cambodia_end + self.canada_end + self.chile_end + self.columbia_end + self.croatia_end + self.czech_end + self.domrep_end + self.ecuador_end + self.egypt_end + self.estonia_end + self.finland_end + self.france_end + self.germany_end + self.greece_end + self.guatemala_end + self.haiti_end + self.hungary_end + self.india_end + self.indonesia_end + self.ireland_end + self.israel_end + self.italy_end + self.latvia_end + self.lebanon_end + self.lithuania_end + self.luxemborg_end + self.macedonia_end + self.malaysia_end + self.mongolia_end + self.newzealand_end + self.nigeria_end + self.norway_end + self.oman_end + self.pakistan_end + self.peru_end + self.philippines_end + self.poland_end + self.portugal_end + self.romania_end + self.russia_end + self.serbia_end + self.singapore + self.singapore_end + self.slovokia_end + self.slovenia_end + self.spain_end + self.sweden_end + self.switzerland_end + self.ukraine_end + self.uk_end + self.usa_end + self.uzbekistan_end
		return list(OrderedDict.fromkeys(mlist))

	def type(self):
		
		type_set = []

		# Professional Limited Liability Company - PLLC=
		for item in self.pllc:
			if item in (self.corpname).lower():
				type_set.append("Professional Limited Liability Company")
				break

		# Limited Liability Limited Partnership
		for item in self.lllp:
			if item in (self.corpname).lower():
				type_set.append("Limited Liability Limited Partnership")
				break

		# Corporation
		for item in self.corp:
			if item in (self.corpname).lower():
				type_set.append("Corporation")
				break

		# Corporation - string end
		if "Corporation" not in type_set:
			for item in self.corp_end:
				if (((self.corpname).lower()).endswith(item)):
					type_set.append("Corporation")
					break

		# General Partnership
		for item in self.gp:
			if item in (self.corpname).lower():
				type_set.append("General Partnership")
				break

		# General Partnership - string end
		if "General Partnership" not in type_set:
			for item in self.gp_end:
				if (((self.corpname).lower()).endswith(item)):
					type_set.append("General Partnership")
					break

		# Limited Liability Company
		for item in self.llc:
			if item in (self.corpname).lower():
				type_set.append("Limited Liability Company")
				break

		# LLC - string end
		if "Limited Liability Company" not in type_set:
			for item in self.llc_end:
				if (((self.corpname).lower()).endswith(item)):
					type_set.append("Limited Liability Company")
					break

		# Limited Liability Partnership
		for item in self.llp:
			if item in (self.corpname).lower():
				type_set.append("Limited Liability Partnership")
				break

		# Limited Partnership
		for item in self.lp:
			if item in (self.corpname).lower():
				type_set.append("Limited Partnership")
				break

		# Limited Partnership - string end
		if "Limited Partnership" not in type_set:
			for item in self.lp_end:
				if (((self.corpname).lower()).endswith(item)):
					type_set.append("Limited Partnership")
					break

		# Limited Company -- LTD
		for item in self.ltd:
			if item in (self.corpname).lower():
				type_set.append("Limited Company")
				break

		# Limited Company - LTD - string end
		if "Limited Company" not in type_set:
			for item in self.ltd_end:
				if (((self.corpname).lower()).endswith(item)):
					type_set.append("Limited Company")
					break

		# Professional Corporation
		for item in self.pc_comma:
			if item in (self.corpname).lower():
				type_set.append("Professional Corporation")
				break

		# No Liability - Aus - string end
		for item in self.nl_end:
			if (((self.corpname).lower()).endswith(item)):
				type_set.append("No Liability")
				break

		# Sole Proprietorship
		for item in self.sp:
			if item in (self.corpname).lower():
				type_set.append("Sole Proprietorship")
				break

		# Sole Proprietorship - string end
		if "Sole Proprietorship" not in type_set:
			for item in self.sp_end:
				if (((self.corpname).lower()).endswith(item)):
					type_set.append("Sole Proprietorship")
					break

		# Joint Venture - string end
		for item in self.jv_end:
			if (((self.corpname).lower()).endswith(item)):
				type_set.append("Sole Proprietorship")
				break

		# Non-Profit
		for item in self.np:
			if item in (self.corpname).lower():
				type_set.append("Non-Profit")
				break

		# Joint Stock - Unlimited
		for item in self.js:
			if item in (self.corpname).lower():
				type_set.append("Joint Stock")
				break

		# Joint Stock - Unlimited - string end
		if "Joint Stock" not in type_set:
			for item in self.js_end:
				if (((self.corpname).lower()).endswith(item)):
					type_set.append("Joint Stock")
					break

		# Mutual Fund
		for item in self.mf:
			if item in (self.corpname).lower():
				type_set.append("Mutual Fund")
				break

		if type_set == []:
			return None
		else:
			return type_set

	
	def industry(self):
		
		industry_set = []

		# Pharmaceutical
		for item in self.pharma:
			if item in (self.corpname).lower():
				industry_set.append("Pharmaceutical")
				break

		# Biotechnology
		for item in self.biotech:
			if item in (self.corpname).lower():
				industry_set.append("Biotechnology")
				break

		# Education
		for item in self.education:
			if item in (self.corpname).lower():
				industry_set.append("Education")
				break

		# Engineering
		for item in self.engineering:
			if item in (self.corpname).lower():
				industry_set.append("Engineering")
				break

		if industry_set == []:
			return None
		else:
			return industry_set


	def country(self):

		country_set = []

		# Albania
		for item in self.albania:
			if item in (self.corpname).lower():
				country_set.append("Albania")
				break

		# Argentina
		for item in self.argentina:
			if item in (self.corpname).lower():
				country_set.append("Argentina")
				break

		# Australia
		for item in self.australia:
			if item in (self.corpname).lower():
				country_set.append("Australia")
				break

		# Austria
		for item in self.austria:
			if item in (self.corpname).lower():
				country_set.append("Austria")
				break

		# Austria -- end string
		if "Austria" not in country_set:
			for item in self.austria_end:
				if (((self.corpname).lower()).endswith(item)):
					type_set.append("Austria")
					break

		# Belarus
		for item in self.belarus:
			if item in (self.corpname).lower():
				country_set.append("Belarus")
				break

		# Belgium
		for item in self.belgium:
			if item in (self.corpname).lower():
				country_set.append("Belgium")
				break
		
		# Belgium -- end string
		if "Belgium" not in country_set:
			for item in self.belgium_end:
				if (((self.corpname).lower()).endswith(item)):
					type_set.append("Belgium")
					break

		# Bosnia / "Herzegovina"
		for item in self.bosherz:
			if item in (self.corpname).lower():
				country_set.append("Bosnia")
				country_set.append("Herzegovina")
				break

		# Brazil
		for item in self.brazil:
			if item in (self.corpname).lower():
				country_set.append("Brazil")
				break

		# Bulgaria -- end string
		for item in self.bulgaria_end:
			if (((self.corpname).lower()).endswith(item)):
				type_set.append("Bulgaria")
				break

		# Cambodia
		for item in self.cambodia:
			if item in (self.corpname).lower():
				country_set.append("Cambodia")
				break

		# Cambodia -- end string
		if "Cambodia" not in country_set:
			for item in self.cambodia_end:
				if (((self.corpname).lower()).endswith(item)):
					type_set.append("Cambodia")
					break

		# Canada
		for item in self.canada:
			if item in (self.corpname).lower():
				country_set.append("Canada")
				break

		# Canada -- end string
		if "Canada" not in country_set:
			for item in self.canada_end:
				if (((self.corpname).lower()).endswith(item)):
					type_set.append("Canada")
					break

		# Chile
		for item in self.chile:
			if item in (self.corpname).lower():
				country_set.append("Chile")
				break

		# Chile -- end string
		if "Chile" not in country_set:
			for item in self.chile_end:
				if (((self.corpname).lower()).endswith(item)):
					type_set.append("Chile")
					break

		# Columbia
		for item in self.columbia:
			if item in (self.corpname).lower():
				country_set.append("Columbia")
				break

		# Columbia -- end string
		if "Columbia" not in country_set:
			for item in self.columbia_end:
				if (((self.corpname).lower()).endswith(item)):
					type_set.append("Columbia")
					break

		# Croatia
		for item in self.croatia:
			if item in (self.corpname).lower():
				country_set.append("Croatia")
				break

		# Croatia -- end string
		if "Croatia" not in country_set:
			for item in self.croatia_end:
				if (((self.corpname).lower()).endswith(item)):
					type_set.append("Croatia")
					break

		# Czech Republic
		for item in self.czech:
			if item in (self.corpname).lower():
				country_set.append("Czech Republic")
				break

		# Czech Republic -- end string
		if "Czech Republic" not in country_set:
			for item in self.czech_end:
				if (((self.corpname).lower()).endswith(item)):
					type_set.append("Czech Republic")
					break

		# Denmark
		for item in self.denmark:
			if item in (self.corpname).lower():
				country_set.append("Denmark")
				break

		# Dominican Republic
		for item in self.domrep:
			if item in (self.corpname).lower():
				country_set.append("Dominican Republic")
				break

		# Dominican Republic -- end string
		if "Dominican Republic" not in country_set:
			for item in self.domrep_end:
				if (((self.corpname).lower()).endswith(item)):
					type_set.append("Dominican Republic")
					break

		# Ecuador
		for item in self.domrep:
			if item in (self.corpname).lower():
				country_set.append("Ecuador")
				break

		# Ecuador -- end string
		if "Ecuador" not in country_set:
			for item in self.domrep_end:
				if (((self.corpname).lower()).endswith(item)):
					type_set.append("Ecuador")
					break

		# Egypt -- end string
		for item in self.egypt_end:
			if (((self.corpname).lower()).endswith(item)):
				type_set.append("Egypt")
				break

		# Estonia -- end string
		for item in self.estonia_end:
			if (((self.corpname).lower()).endswith(item)):
				type_set.append("Estonia")
				break

		# Finland
		for item in self.finland:
			if item in (self.corpname).lower():
				country_set.append("Finland")
				break

		# Finland -- end string
		if "Finland" not in country_set:
			for item in self.finland_end:
				if (((self.corpname).lower()).endswith(item)):
					type_set.append("Finland")
					break

		# France
		for item in self.france:
			if item in (self.corpname).lower():
				country_set.append("France")
				break

		# France -- end string
		if "France" not in country_set:
			for item in self.france_end:
				if (((self.corpname).lower()).endswith(item)):
					type_set.append("France")
					break

		# Germany
		for item in self.germany:
			if item in (self.corpname).lower():
				country_set.append("Germany")
				break

		# Germany -- end string
		if "Germany" not in country_set:
			for item in self.germany_end:
				if (((self.corpname).lower()).endswith(item)):
					type_set.append("Germany")
					break

		# Greece -- end string
		for item in self.greece_end:
			if (((self.corpname).lower()).endswith(item)):
				type_set.append("Greece")
				break

		# Guatemala -- end string
		for item in self.guatemala_end:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Guatemala")
				break

		# Haiti -- end string
		for item in self.haiti_end:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Haiti")
				break

		# Hong Kong
		for item in self.hongkong:
			if item in (self.corpname).lower():
				country_set.append("Hong Kong")
				break

		# Hungary
		for item in self.hungary:
			if item in (self.corpname).lower():
				country_set.append("Hungary")
				break

		# Hungary -- end string
		if "Hungary" not in country_set:
			for item in self.hungary_end:
				if (((self.corpname).lower()).endswith(item)):
					type_set.append("Hungary")
					break

		# Iceland
		for item in self.iceland:
			if item in (self.corpname).lower():
				country_set.append("Iceland")
				break

		# India
		for item in self.india:
			if item in (self.corpname).lower():
				country_set.append("India")
				break

		# India -- end string
		if "India" not in country_set:
			for item in self.india_end:
				if (((self.corpname).lower()).endswith(item)):
					country_set.append("India")
					break

		# Indonesia -- end string
		for item in self.indonesia_end:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Indonesia")
				break

		# Ireland -- end string
		for item in self.ireland_end:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Ireland")
				break

		# Israel -- end string
		for item in self.israel_end:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Israel")
				break

		# Italy
		for item in self.italy:
			if item in (self.corpname).lower():
				country_set.append("Italy")
				break

		# Italy -- end string
		if "Italy" not in country_set:
			for item in self.italy_end:
				if (((self.corpname).lower()).endswith(item)):
					type_set.append("Italy")
					break

		# Latvia -- end string
		for item in self.latvia_end:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Latvia")
				break

		# Lebanon -- end string
		for item in self.lebanon_end:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Lebanon")
				break

		# Lithuania -- end string
		for item in self.lithuania_end:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Lithuania")
				break

		# Luxemborg
		for item in self.luxemborg:
			if item in (self.corpname).lower():
				country_set.append("Luxemborg")
				break

		# Luxemborg -- end string
		if "Luxemborg" not in country_set:
			for item in self.luxemborg_end:
				if (((self.corpname).lower()).endswith(item)):
					country_set.append("Luxemborg")
					break

		# Macedonia
		for item in self.macedonia:
			if item in (self.corpname).lower():
				country_set.append("Macedonia")
				break

		# Macedonia -- end string
		if "Macedonia" not in country_set:
			for item in self.macedonia_end:
				if (((self.corpname).lower()).endswith(item)):
					country_set.append("Macedonia")
					break

		# Malaysia -- end string
		for item in self.malaysia_end:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Malaysia")
				break

		# Mexico
		for item in self.mexico:
			if item in (self.corpname).lower():
				country_set.append("Mexico")
				break

		# Mongolia -- end string
		for item in self.mongolia_end:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Mongolia")
				break

		# Netherlands
		for item in self.netherlands:
			if item in (self.corpname).lower():
				country_set.append("Netherlands")
				break

		# New Zealand
		for item in self.newzealand:
			if item in (self.corpname).lower():
				country_set.append("New Zealand")
				break

		# New Zealand -- end string
		if "New Zealand" not in country_set:
			for item in self.newzealand_end:
				if (((self.corpname).lower()).endswith(item)):
					country_set.append("New Zealand")
					break

		# Nigeria
		for item in self.nigeria:
			if item in (self.corpname).lower():
				country_set.append("Nigeria")
				break

		# Nigeria -- end string
		if "Nigeria" not in country_set:
			for item in self.nigeria_end:
				if (((self.corpname).lower()).endswith(item)):
					country_set.append("Nigeria")
					break

		# Norway -- end string
		for item in self.norway_end:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Norway")
				break

		# Oman -- end string
		for item in self.oman_end:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Oman")
				break

		# Pakistan
		for item in self.pakistan:
			if item in (self.corpname).lower():
				country_set.append("Pakistan")
				break

		# Pakistan -- end string
		if "Pakistan" not in country_set:
			for item in self.pakistan_end:
				if (((self.corpname).lower()).endswith(item)):
					country_set.append("Pakistan")
					break

		# Peru -- end string
		for item in self.peru_end:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Peru")
				break

		# Philippines -- end string
		for item in self.philippines_end:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Philippines")
				break

		# Poland
		for item in self.poland:
			if item in (self.corpname).lower():
				country_set.append("Poland")
				break

		# Poland -- end string
		if "Poland" not in country_set:
			for item in self.poland_end:
				if (((self.corpname).lower()).endswith(item)):
					country_set.append("Poland")
					break

		# Portugal
		for item in self.portugal:
			if item in (self.corpname).lower():
				country_set.append("Portugal")
				break

		# Portugal -- end string
		if "Portugal" not in country_set:
			for item in self.portugal_end:
				if (((self.corpname).lower()).endswith(item)):
					country_set.append("Portugal")
					break

		# Romania
		for item in self.romania:
			if item in (self.corpname).lower():
				country_set.append("Romania")
				break

		# Romania -- end string
		if "Romania" not in country_set:
			for item in self.romania_end:
				if (((self.corpname).lower()).endswith(item)):
					country_set.append("Romania")
					break

		# Russia -- end string
		for item in self.russia_end:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Russia")
				break

		# Serbia
		for item in self.serbia:
			if item in (self.corpname).lower():
				country_set.append("Serbia")
				break

		# Serbia -- end string
		if "Serbia" not in country_set:
			for item in self.serbia_end:
				if (((self.corpname).lower()).endswith(item)):
					country_set.append("Serbia")
					break

		# Singapore
		for item in self.singapore:
			if item in (self.corpname).lower():
				country_set.append("Singapore")
				break

		# Singapore -- end string
		if "Singapore" not in country_set:
			for item in self.singapore_end:
				if (((self.corpname).lower()).endswith(item)):
					country_set.append("Singapore")
					break

		# Slovokia -- end string
		for item in self.slovokia_end:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Slovokia")
				break

		# Slovenia -- end string
		for item in self.slovenia_end:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Slovenia")
				break

		# Spain -- end string
		for item in self.spain_end:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Spain")
				break

		# Sweden -- end string
		for item in self.sweden_end:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Sweden")
				break

		# Switzerland -- end string
		for item in self.switzerland_end:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Switzerland")
				break

		# Turkey
		for item in self.turkey:
			if item in (self.corpname).lower():
				country_set.append("Turkey")
				break

		# Ukraine -- end string
		for item in self.ukraine_end:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Ukraine")
				break

		# United Kingdom
		for item in self.uk:
			if item in (self.corpname).lower():
				country_set.append("United Kingdom")
				break

		# United Kingdom -- end string
		if "United Kingdom" not in country_set:
			for item in self.uk_end:
				if (((self.corpname).lower()).endswith(item)):
					country_set.append("United Kingdom")
					break

		# United States
		for item in self.usa:
			if item in (self.corpname).lower():
				country_set.append("United States")
				break

		# United States -- end string
		if "United States" not in country_set:
			for item in self.usa_end:
				if (((self.corpname).lower()).endswith(item)):
					country_set.append("United States")
					break

		# Uzbekistan -- end string
		for item in self.uzbekistan_end:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Uzbekistan")
				break

		if country_set == []:
			return None
		else:
			return country_set


	# A clean version of the business name
	def cleanname(self):

		corpname = self.corpname

		# Get rid of comma-denoted end strings
		# Professional corporation
		for item in self.pc_comma:
			if item in corpname.lower():
				start = (corpname.lower()).find(item)
				end = len(corpname)
				corpname = corpname[0:start] + corpname[end+1:len(corpname)]
		
		# Strip out commas
		if "," in corpname:
			corpname = corpname.replace(",", " ")

		# Get rid of non-end items
		for item in self.masterlist():
			if item in corpname.lower():
				start = (corpname.lower()).find(item)
				end = len(corpname)
				corpname = corpname[0:start] + corpname[end+1:len(corpname)]

		# Get rid of endswith items:
		for item in self.masterlist_end():
			if ((corpname.lower()).endswith(item)):
				start = (corpname.lower()).find(item)
				end = len(item)
				end = end * -1
				corpname = corpname[0:end]

		# Abbrv. cleanup
		for abbv in self.abbv:
			if abbv in corpname.lower():
				start = (corpname.lower()).find(abbv)
				end = len(corpname)
				corpname = corpname[0:start] + self.abbv[abbv] + corpname[end+1:len(corpname)]

		# Strip spaces on the left
		corpname = corpname.lstrip()

		#Strip spaces on the right
		corpname = corpname.strip()

		# Get rid of misc spaces in between
		corpname = " ".join(corpname.split())

		return corpname


	# A short version of the corporate name
	def shortname(self):

		corpname = self.corpname

		# Run the corpname through cleanname first
		corpname = self.cleanname()
		
		# Get rid of everything in parenthesis
		if " (" and ")" in corpname:
			beginpar = corpname.find(" (")
			endpar = corpname.find(")")
			corpname = corpname.replace(corpname[beginpar:endpar+1],"")

		# Get rid of everything after hyphens
		if " - " in corpname:
			corplen = len(corpname)
			hypenloc = corpname.find(" - ")
			corpname = corpname.replace(corpname[hypenloc:corplen],"")

		# Get rid of misc spaces in between
		corpname = " ".join(corpname.split())

		# Strip spaces on the left
		corpname = corpname.lstrip()

		#Strip spaces on the right
		corpname = corpname.strip()

		return corpname