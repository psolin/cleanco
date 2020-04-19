from clean import get_terms, basename
from classify import typesources, countrysources


class cleanco:
   "silly backwards compatibility wrapper, you should NOT use this"

   def __init__(self):
      self._types = typesources()
      self._countries = countrysources()
      self._terms = get_terms()

   def clean_name(self, name):
      return basename(name, self._terms)

   def country(self, name):
      return matches(name, self._countries)

   def type(self, name):
      return matches(name, self._types)
