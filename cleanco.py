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

		# LP - Limited Partnership
		self.lp = ["gmbh & co. kg", "gmbh & co. kg", " lp", "l.p.", "s.c.s.", "s.c.p.a", "comm.v", "k.d.", "k.d.a.", "s. en c.", "e.e.", "s.a.s.", "s. en c.", "c.v.", "s.k.a.", "sp.k.", "s.cra.", " ky", " scs", " kg", " kd", " k/s", " ee", " secs", " kda", " ks", " kb", " kt"]

		# Corporation
		self.corporation = ["incorporated", "corporation", "corp", " inc", " & co.", "inc.", "s.p.a.", "n.v.", " a.g.", " ag", " nuf", " s.a.", " s.f.", " oao"]

		# GP - General Partnership
		self.gp = ["soc.col.", "stg", "d.n.o.", "ltda.", "v.o.s.", "kgaa", "o.e.", "s.f.", "s.n.c.", "s.a.p.a.", "j.t.d.", "v.o.f.", "sp.j.", " og", " sd", " vos", " i/s", " ay", " snc", " oe", " bt.", " s.s.", " mb", " ans", " da", " o.d.", " hb", "pt"]

		# LLC - Limited Liability Company (PLC - UK)
		self.llc = ["pllc", "llc", "l.l.c.", "plc", "hf.", "oyj", "a.e.", "nyrt.", "p.l.c.", "sh.a.", "s.a.", "s.r.l.", "srl.", "aat", "3at", "d.d.", "akc. spol.", "a.s.", "s.r.o.", "s.m.b.a.", "smba", "sarl", " nv", " sa", " aps", " a/s", " p/s", " sae", " sasu", "eurl", " ae", " cpt", " as", " ab", " asa", " ooo", " dat", " vat", " zat", " mchj", " a.d."]
		
		# LLP - Limited Liability Partnership
		self.llp = ["llp", "l.l.p.", "sp.p.", "s.c.a.", "s.c.s."]
		
		# Ltd - Private Company Limited By Shares - UK
		self.ltd = ["pty. ltd.", "pty ltd", "ltd", "l.t.d.", "bvba", "d.o.o.", "ltda", "gmbh", "g.m.b.h", "kft.", "kht.", "zrt.", "ehf.", "s.a.r.l.", "d.o.o.e.l.", "s. de r.l.", "b.v.", "tapui", "sp. z.o.o.", "s.r.l.", "s.l.", "s.l.n.e.", " ood", " oy", " rt.", " teo", " uab", " scs", " sprl", " limited", " bhd.", " sdn. bhd.", " sdn bhd", " as", " lda.", " tov", " pp"]
		
		# PC - Professional Corporation -- contains a comma
		self.pc_comma = ["p.c.", ", pc", "vof", "snc"]

		# NL - No Liability - Australia
		self.nl = [" nl"]

		# SP - Sole Proprietorship
		self.sp = ["e.u.", "s.p.", "t:mi", "e.v.", "e.c.", " et", " obrt", " fie", " ij", " fop", " xt"]

		# Joint Stock - Unlimited
		self.js = ["unltd", "ultd", " sal", "unlimited", " saog", " saoc", " aj", " yoaj", " oaj"]

		# Joint Venture
		self.jv = [" esv", " gie", " kv.", " qk"]

		# Non-Profit
		self.np = ["vzw", "ses.", "gte."]

		# Mutual Fund
		self.mf = ["sicav"]

		# Countries that can be identified due to specific business types in the name -- thanks Wikipedia!
		self.albania = ["sh.a.", "sh.p.k."]
		self.argentina = ["s.a.", "s.r.l.", "s.c.p.a", " scpa", "s.c.e i.", "s.e.", "s.g.r", "soc.col."]
		self.australia = [" nl", "pty. ltd.", "pty ltd"]
		self.austria = ["e.u.", "stg", "gesbr", "a.g.", " ag", " og", " kg"]
		self.belarus = ["aat", "3at"]
		self.belgium = ["esv", "vzw", "vof", "snc", "comm.v", "scs", "bvba", "sprl", "cbva", "cvoa", " sca", " sep", " gie"]
		self.bosherz = ["d.d.", " a.d.", "d.n.o.", "d.o.o.", "k.v.", "s.p."]
		self.bulgaria = [" ad", "adsitz", " ead", " et", "kd", "kda", " sd"]
		self.brazil = ["ltda", "s.a.", "pllc", " ad", "adsitz", " ead", " et", "kd", "kda", " sd"]
		self.cambodia = ["gp", "sm pte ltd.", "pte ltd.", "plc ltd.", "peec", " sp"]
		self.canada = ["gp", " lp", " sp"]
		self.chile = ["eirl", "s.a.", "sgr", "s.g.r.", "ltda", "s.p.a.", " sa", "s. en c.", "ltda."]
		self.columbia = ["s.a.", "e.u.", "s.a.s.", "suc. de descendants", " sca"]
		self.croatia = ["d.d.", "d.d.o.", " obrt"]
		self.czech = ["a.s.", "akc. spol.", "s.r.o.", "v.o.s.", "k.s.", " sro", " vos"]
		self.denmark = [" i/s", " a/s", " k/s", " p/s", "amba", "a.m.b.a.", "fmba", "f.m.b.a.", "smba", "s.m.b.a.", " g/s"]
		self.domrep = [" c. por a.", "cxa", "s.a.", "s.a.s.", "srl.", "eirl.", " sa", " sas"]
		self.ecuador = ["s.a.", "c.a.", " sa", " ep"]
		self.egypt = [" sae"]
		self.estonia = [" fie"]
		self.finland = ["t:mi", " ay", " ky", " oy", " oyj", " ok"]
		self.france = ["sicav", "sarl", "sogepa", " ei", " eurl", " sasu", " fcp", " gie", " sep", " snc", " scs", " sca", " scop", " sem", " sas"]
		self.germany = ["gmbh & co. kg", "gmbh & co. kg", "e.g.", "e.v.", "gbr", "ohg", "partg", "kgaa", "gmbh", "g.m.b.h.", " ag"]
		self.greece = [" a.e.", " ae", "e.e.", " ee", " epe", "e.p.e.", " mepe", "m.e.p.e.", "o.e.", " oe", " ovee", "o.v.e.e."]
		self.guatemala = [" s.a.", " sa"]
		self.haiti = [" sa"]
		self.hongkong = ["ltd", "unltd", "ultd"]
		self.hungary = ["e.v.", "e.c.", "bt.", "kft.", "kht.", "kkt.", "k.v.", "zrt.", "nyrt", " ev", " ec", " rt."]
		self.iceland = ["ehf.", "hf.", "ohf.", "s.f.", "ses."]
		self.india = ["pvt. ltd.", "ltd.", " psu", " pse"]
		self.indonesia = [" ud", " fa", " pt"]
		self.ireland = [" cpt", " teo"]
		self.israel = [" b.m.", " bm", " ltd"]
		self.italy = ["s.n.c.", "s.a.s.", "s.p.a.", "s.a.p.a.", "s.r.l.", "s.c.r.l.", " s.s."]
		self.latvia = [" as", " sia", " ik", " ps", " ks"]
		self.lebanon = [" sal"]
		self.lithuania = [" uab", " ab", " ij", " mb"]
		self.luxemborg = ["s.a.", "s.a.r.l.", " secs"]
		self.macedonia = ["d.o.o.", "d.o.o.e.l", "k.d.a.", "j.t.d.", " a.d.", " k.d."]
		self.malaysia = [" bhd.", "sdn. bhd."]
		self.mexico = ["s.a.", "s. de. r.l.", "s. en c.", "s.a.b.", "s.a.p.i."]
		self.mongolia = [" xk", " xxk"]
		self.netherlands = ["v.o.f.", "c.v.", "b.v.", "n.v."]
		self.newzealand = ["tapui", " ltd"]
		self.nigeria = ["gte.", "plc", " ltd.", "ultd."]
		self.norway = [" asa", " as", " ans", " ba", " bl", " da", " etat", "fkf", " hf", " iks", " kf", " ks", " nuf", " rhf", " sf"]
		self.oman = ["saog", "saoc"]
		self.pakistan = ["ltd.", "pvt. ltd.", " ltd"]
		self.peru = [" sa", " s.a.", " s.a.a."]
		self.philippines = [" coop.", " corp.", " corp", " ent.", " inc.", " inc", " llc", " l.l.c.", " ltd."]
		self.poland = ["p.p.", "s.k.a.", "sp.j.", "sp.k.", "sp.p.", "sp. z.o.o.", " s.c.", " s.a."]
		self.portugal = ["lda.", " crl", " s.a.", " s.f.", " sgps"]
		self.romania = ["s.c.a.", "s.c.s.", "s.n.c.", "s.r.l.", "o.n.g.", " s.a."]
		self.russia = [" ooo", " oao", " zao", " 3ao"]
		self.serbia = ["d.o.o.", " a.d.", " k.d.", " o.d."]
		self.singapore = ["bhd", "pte ltd", "sdn bhd", "llp", " l.l.p.", " ltd.", "pte"]
		self.slovokia = [" a.s.", " s.r.o.", " k.s.", " v.o.s."]
		self.slovenia = [" d.d.", " d.o.o.", " d.n.o.", " k.d.", " s.p."]
		self.spain = [" s.a.", " s.a.d.", " s.l.", " s.l.l.", " s.l.n.e.", " s.c.", " s.cra", " s.coop", " sal", " sccl"]
		self.sweden = [" ab", " hb", " kb"]
		self.switzerland = [" ab", " sa", " gmbh", " g.m.b.h.", " sarl", " sagl"]
		self.turkey = [" koop."]
		self.ukraine = [" dat", " fop", " kt", " pt", " tdv", " tov", " pp", " vat", " zat", " at"]
		self.uk = ["plc", " uk", " cic", " cio", " l.l.p.", " llp", " l.p.", " lp", " ltd.", " ltd"]
		self.usa = [" inc.", "corporation", "incorporated" "company", "limited", "corp.", "inc.", "inc", "llp", "l.l.p.", "pllc", " and company", " & company", " usa", " inc", " inc.", " corp.", " corp", " ltd.", "ltd", " & co."," co.", " co", " lp", ", pc"]
		self.uzbekistan = [" mchj", " qmj", " aj", " oaj", " yoaj", " xk", " xt", " ok" " uk", " qk"]

		# Private company?
		self.pte = ["private", "pte", " xk"]

		
		## Abbreviations ##
		self.abbv  = {'intl.':'International', 'intl':'International', 'co.':'Company', 'mfg':'Manufacturing'}

		# Abbreviations when strings end with these
		self.abbvend = {' co':'Company'}


		## Industry ##
		self.busind = ["Pharmaceutical, Biotechnology", "Engineering"]
		self.pharma = [" therap", "biopharmaceuticals", "biopharmaceutical", "biopharma", "biopharm", "pharmaceuticals", "pharmaceutical", "pharma"]
		self.biotech = [" therap", "biopharmaceuticals", "biopharmaceutical", "biopharma", "biopharm", "biotechnology", "biotechnologies", "bioventures", "biolabs", "biosciences", "bioscience", "biotech"]
		self.engineering = ["engineer"]
		self.education = ["education", "university", "school of", "academy"]

	def masterlist(self):
		mlist = self.pllc + self.lllp + self.lp + self.corporation + self.gp + self.llc + self.llp + self.ltd + self.pc_comma + self.nl + self.sp + self.js + self.jv + self.np + self.mf + self.albania + self.argentina + self.australia + self.austria + self.belarus + self.belgium + self.bosherz + self.bulgaria + self.brazil + self.cambodia + self.canada + self.chile + self.columbia + self.croatia + self.czech + self.denmark + self.domrep + self.ecuador + self.egypt + self.estonia + self.finland + self.france + self.germany + self.greece + self.guatemala + self.haiti + self.hongkong + self.hungary + self.iceland + self.india + self.indonesia + self.ireland + self.israel + self.italy + self.latvia + self.lebanon + self.lithuania + self.luxemborg + self.macedonia + self.malaysia + self.mexico + self.mongolia + self.netherlands + self.newzealand + self.nigeria + self.norway + self.oman + self.pakistan + self.peru + self.philippines + self.poland + self.portugal + self.romania + self.russia + self.serbia + self.singapore + self.slovokia + self.slovenia + self.spain + self.sweden + self.switzerland + self.turkey + self.ukraine + self.uk + self.usa + self.uzbekistan
		return list(OrderedDict.fromkeys(mlist))

	def type(self):
		
		type_set = []

		# Limited Partnership
		for item in self.lp:
			if (((self.corpname).lower()).endswith(item)):
				type_set.append("Limited Partnership")
				break

		# Professional Limited Liability Company - PLLC
		for item in self.pllc:
			if (((self.corpname).lower()).endswith(item)):
				type_set.append("Professional Limited Liability Company")
				break

		# Limited Liability Limited Partnership
		for item in self.lllp:
			if (((self.corpname).lower()).endswith(item)):
				type_set.append("Limited Liability Limited Partnership")
				break

		# Corporation
		for item in self.corporation:
			if (((self.corpname).lower()).endswith(item)):
				type_set.append("Corporation")
				break

		# General Partnership
		for item in self.gp:
			if (((self.corpname).lower()).endswith(item)):
				type_set.append("General Partnership")
				break

		# Limited Liability Company
		for item in self.llc:
			if (((self.corpname).lower()).endswith(item)):
				type_set.append("Limited Liability Company")
				break

		# Limited Liability Partnership
		for item in self.llp:
			if (((self.corpname).lower()).endswith(item)):
				type_set.append("Limited Liability Partnership")
				break

		# Limited Company -- LTD
		for item in self.ltd:
			if (((self.corpname).lower()).endswith(item)):
				type_set.append("Limited Company")
				break

		# Professional Corporation
		for item in self.pc_comma:
			if (((self.corpname).lower()).endswith(item)):
				type_set.append("Professional Corporation")
				break

		# No Liability - Aus
		for item in self.nl:
			if (((self.corpname).lower()).endswith(item)):
				type_set.append("No Liability")
				break

		# Sole Proprietorship
		for item in self.sp:
			if (((self.corpname).lower()).endswith(item)):
				type_set.append("Sole Proprietorship")
				break

		# Joint Venture
		for item in self.jv:
			if (((self.corpname).lower()).endswith(item)):
				type_set.append("Sole Proprietorship")
				break

		# Non-Profit
		for item in self.np:
			if (((self.corpname).lower()).endswith(item)):
				type_set.append("Non-Profit")
				break

		# Joint Stock - Unlimited
		for item in self.js:
			if (((self.corpname).lower()).endswith(item)):
				type_set.append("Joint Stock")
				break

		# Mutual Fund
		for item in self.mf:
			if (((self.corpname).lower()).endswith(item)):
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
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Albania")
				break

		# Argentina
		for item in self.argentina:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Argentina")
				break

		# Australia
		for item in self.australia:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Australia")
				break

		# Austria
		for item in self.austria:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Austria")
				break

		# Belarus
		for item in self.belarus:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Belarus")
				break

		# Belgium
		for item in self.belgium:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Belgium")
				break

		# Bosnia / "Herzegovina"
		for item in self.bosherz:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Bosnia")
				country_set.append("Herzegovina")
				break

		# Brazil
		for item in self.brazil:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Brazil")
				break

		# Bulgaria
		for item in self.bulgaria:
			if (((self.corpname).lower()).endswith(item)):
				type_set.append("Bulgaria")
				break

		# Cambodia
		for item in self.cambodia:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Cambodia")
				break

		# Canada
		for item in self.canada:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Canada")
				break

		# Chile
		for item in self.chile:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Chile")
				break

		# Columbia
		for item in self.columbia:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Columbia")
				break

		# Croatia
		for item in self.croatia:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Croatia")
				break

		# Czech Republic
		for item in self.czech:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Czech Republic")
				break

		# Denmark
		for item in self.denmark:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Denmark")
				break

		# Dominican Republic
		for item in self.domrep:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Dominican Republic")
				break

		# Ecuador
		for item in self.ecuador:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Ecuador")
				break

		# Egypt
		for item in self.egypt:
			if (((self.corpname).lower()).endswith(item)):
				type_set.append("Egypt")
				break

		# Estonia
		for item in self.estonia:
			if (((self.corpname).lower()).endswith(item)):
				type_set.append("Estonia")
				break

		# Finland
		for item in self.finland:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Finland")
				break

		# France
		for item in self.france:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("France")
				break

		# Germany
		for item in self.germany:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Germany")
				break

		# Greece
		for item in self.greece:
			if (((self.corpname).lower()).endswith(item)):
				type_set.append("Greece")
				break

		# Guatemala
		for item in self.guatemala:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Guatemala")
				break

		# Haiti
		for item in self.haiti:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Haiti")
				break

		# Hong Kong
		for item in self.hongkong:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Hong Kong")
				break

		# Hungary
		for item in self.hungary:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Hungary")
				break

		# Iceland
		for item in self.iceland:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Iceland")
				break

		# India
		for item in self.india:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("India")
				break

		# Indonesia
		for item in self.indonesia:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Indonesia")
				break

		# Ireland
		for item in self.ireland:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Ireland")
				break

		# Israel
		for item in self.israel:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Israel")
				break

		# Italy
		for item in self.italy:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Italy")
				break

		# Latvia
		for item in self.latvia:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Latvia")
				break

		# Lebanon
		for item in self.lebanon:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Lebanon")
				break

		# Lithuania
		for item in self.lithuania:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Lithuania")
				break

		# Luxemborg
		for item in self.luxemborg:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Luxemborg")
				break

		# Macedonia
		for item in self.macedonia:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Macedonia")
				break

		# Malaysia
		for item in self.malaysia:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Malaysia")
				break

		# Mexico
		for item in self.mexico:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Mexico")
				break

		# Mongolia
		for item in self.mongolia:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Mongolia")
				break

		# Netherlands
		for item in self.netherlands:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Netherlands")
				break

		# New Zealand
		for item in self.newzealand:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("New Zealand")
				break

		# Nigeria
		for item in self.nigeria:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Nigeria")
				break

		# Norway
		for item in self.norway:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Norway")
				break

		# Oman
		for item in self.oman:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Oman")
				break

		# Pakistan
		for item in self.pakistan:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Pakistan")
				break

		# Peru
		for item in self.peru:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Peru")
				break

		# Philippines
		for item in self.philippines:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Philippines")
				break

		# Poland
		for item in self.poland:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Poland")
				break

		# Portugal
		for item in self.portugal:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Portugal")
				break

		# Romania
		for item in self.romania:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Romania")
				break

		# Russia
		for item in self.russia:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Russia")
				break

		# Serbia
		for item in self.serbia:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Serbia")
				break

		# Singapore
		for item in self.singapore:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Singapore")
				break

		# Slovokia
		for item in self.slovokia:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Slovokia")
				break

		# Spain
		for item in self.spain:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Spain")
				break

		# Sweden
		for item in self.sweden:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Sweden")
				break

		# Switzerland
		for item in self.switzerland:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Switzerland")
				break

		# Turkey
		for item in self.turkey:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Turkey")
				break

		# Ukraine
		for item in self.ukraine:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("Ukraine")
				break

		# United Kingdom
		for item in self.uk:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("United Kingdom")
				break

		# United States
		for item in self.usa:
			if (((self.corpname).lower()).endswith(item)):
				country_set.append("United States")
				break

		# Uzbekistan
		for item in self.uzbekistan:
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

		# Get rid of country items:
		for item in self.masterlist():
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

		# Strip out commas
		if "," in corpname:
			corpname = corpname.replace(",", " ")

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