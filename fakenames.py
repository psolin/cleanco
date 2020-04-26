from faker import Faker
locales = ("ru_RU", "fi_FI", "en_UK", "en_US", "fr_FR", "de_DE", "sv_SE", "pl_PL", "es_ES")

TESTNAMES = []

for l in locales:
   fake = Faker(l)
   TESTNAMES += [fake.company() for n in range(500)]

