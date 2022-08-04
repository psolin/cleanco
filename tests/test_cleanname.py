# encoding: utf-8
import pytest
from cleanco import basename


def test_deterministic_terms(monkeypatch):
   """prepare_default_terms should always return the same list (even for different ordering in get_unique_terms)"""
   from cleanco import clean
   with monkeypatch.context() as m:
      mock_terms = ["aaa", "bbb", "ccc"]
      m.setattr(clean, "get_unique_terms", lambda: mock_terms)
      res1 = clean.prepare_default_terms()
      m.setattr(clean, "get_unique_terms", lambda: reversed(mock_terms))
      res2 = clean.prepare_default_terms()
      assert res1 == res2


# Tests that demonstrate stuff is stripped away

basic_cleanup_tests = {
   "name w/ suffix":           "Hello World Oy",
   "name w/ ', ltd.'":         "Hello World, ltd.",
   "name w/ ws suffix ws":     "Hello    World ltd",
   "name w/ suffix ws":        "Hello World ltd ",
   "name w/ suffix dot ws":    "Hello World ltd. ",
   "name w/ ws suffix dot ws": " Hello World ",
   "name w/ suffix including accents and whitespace": "Hello World S.à r.l."
}

def test_basic_cleanups():
   expected = "Hello World"
   errmsg = "cleanup of %s failed"
   for testname, variation in basic_cleanup_tests.items():
      assert basename(variation) == expected, errmsg % testname

multi_cleanup_tests = {
   "name + suffix":          "Hello World Oy",
   "name + suffix (without punct)":          "Hello World sro",
   "prefix + name":          "Oy Hello World",
   "prefix + name + suffix": "Oy Hello World Ab",
   "name w/ term in middle": "Hello Oy World",
   "name w/ complex term in middle": "Hello pty ltd World",
   "name w/ mid + suffix":   "Hello Oy World Ab"
}

def test_multi_type_cleanups():
   expected = "Hello World"
   errmsg = "cleanup of %s failed"
   for testname, variation in multi_cleanup_tests.items():
      result = basename(variation, prefix=True, suffix=True, middle=True)
      assert result == expected, errmsg % testname


# Tests that demonstrate basename can be run twice effectively

double_cleanup_tests = {
   "name + two prefix":      "Ab Oy Hello World",
   "name + two prefix":      "Hello World Ab Ltd",
   "name + two suffix":      "Hello World Ab Oy",
   "name + two in middle":   "Hello Ab Oy World"
}

def test_double_cleanups():
   expected = "Hello World"
   errmsg = "cleanup of %s failed"
   for testname, variation in multi_cleanup_tests.items():
      result = basename(variation, prefix=True, suffix=True, middle=True)
      final = basename(result, prefix=True, suffix=True, middle=True)

      assert final == expected, errmsg % testname

# Tests that demonstrate organization name is kept intact

preserving_cleanup_tests = {
   "name with comma": ("Hello, World, ltd.", "Hello, World"),
   "name with dot": ("Hello. World, Oy", "Hello. World")
}

def test_preserving_cleanups():
   errmsg = "preserving cleanup of %s failed"
   for testname, (variation, expected) in preserving_cleanup_tests.items():
      assert basename(variation) == expected, errmsg % testname

# Test umlauts


unicode_umlaut_tests = {
   "name with umlaut in end": ("Säätämö Oy", "Säätämö"),
   "name with umlauts & comma": ("Säätämö, Oy", "Säätämö"),
   "name with no ending umlaut": ("Säätämo Oy", "Säätämo"),
   "name with beginning umlaut": ("Äätämo Oy", "Äätämo"),
   "name with just umlauts": ("Äätämö", "Äätämö"),
   "cyrillic name": ("ОАО Новороссийский морской торговый порт", "Новороссийский морской торговый порт")

}

def test_with_unicode_umlauted_name():
   errmsg = "preserving cleanup of %s failed"
   for testname, (variation, expected) in unicode_umlaut_tests.items():
      assert basename(variation, prefix=True) == expected, errmsg % testname


terms_with_accents_tests = {
   "term with ł correct spelling": ("Łoś spółka z o.o", "Łoś"),
   "term with ł incorrect spelling": ("Łoś spolka z o.o", "Łoś"),
}

def test_terms_with_accents():
   errmsg = "preserving cleanup of %s failed"
   for testname, (variation, expected) in terms_with_accents_tests.items():
      assert basename(variation, suffix=True) == expected, errmsg % testname
