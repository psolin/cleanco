from .clean import prepare_terms, basename
from .classify import typesources, countrysources, matches


class cleanco:
   "silly backwards compatibility wrapper, you should NOT use this"

   def __init__(self, name):
      self._name = name
      self._types = typesources()
      self._countries = countrysources()
      self._terms = prepare_terms()

   def clean_name(self):
      return basename(self._name, self._terms)

   def country(self):
      return matches(self._name, self._countries)

   def type(self):
      return matches(self._name, self._types)
