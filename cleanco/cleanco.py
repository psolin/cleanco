from .clean import basename
from .classify import typesources, countrysources, matches


class cleanco:
   "silly backwards compatibility wrapper, you should NOT use this"

   def __init__(self, name):
      self._name = name
      self._types = typesources()
      self._countries = countrysources()

   def clean_name(self):
      return basename(self._name)

   def country(self):
      return matches(self._name, self._countries)

   def type(self):
      return matches(self._name, self._types)
