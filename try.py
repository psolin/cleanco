#from cleanco.classify import matches, typesources, countrysources
from cleanco.clean import basename_strcmp, basename_partcmp, basename_partcmp_oneloop
from cleanco.clean import get_terms, normalize_terms
from fakenames import TESTNAMES
from timeit import timeit


def deconstructed_terms():
   "return (size, parts) list of normalized, deconstructed terms"
   terms = get_terms()
   nterms = normalize_terms(terms)
   ntermparts = (t.split() for t in nterms)
   sntermparts = sorted(ntermparts, key=len, reverse=True)
   return [(len(tp), tp) for tp in sntermparts]

def string_terms():
   terms = get_terms()
   nterms = normalize_terms(terms)
   return tuple(zip(sorted(terms, key=len), sorted(nterms, key=len)))

def remove_terms(testnames, terms, stripterms):
   results = []
   for n1 in TESTNAMES:
      n2 = stripterms(n1, terms,  prefix=True, suffix=True, middle=True)
      while n2 != n1:
         n1 = n2
         n2 = stripterms(n1, terms,  prefix=True, suffix=True, middle=True)
      results.append(n2)
   return results


def compare():
   results1 = test_strcmp()
   results2 = test_partcmp()
   return (set(results1).difference(results2), set(results2).difference(results1))

def compare_partcmp():
   results1 = test_partcmp()
   results2 = test_partcmp_oneloop()
   return (set(results1).difference(results2), set(results2).difference(results1))

def test_strcmp():
   return remove_terms(TESTNAMES, string_terms(), basename_strcmp)

def test_partcmp():
   return remove_terms(TESTNAMES, deconstructed_terms(), basename_partcmp)

def test_partcmp_oneloop():
   return remove_terms(TESTNAMES, deconstructed_terms(), basename_partcmp_oneloop)

print("str cmp: ", timeit(stmt="test_strcmp()", globals=globals(), number=3))
print("part cmp: ", timeit("test_partcmp()", globals=globals(), number=3))
print("part cmp (one loop): ", timeit("test_partcmp_oneloop()", globals=globals(), number=3))
