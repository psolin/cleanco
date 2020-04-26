# encoding: utf-8
import pytest
from cleanco.clean import prepare_terms, basename


@pytest.fixture
def terms():
   return prepare_terms()

# Tests that demonstrate stuff is stripped away

basic_cleanup_tests = {
   "name w/ suffix":           "Hello World Oy",
   "name w/ ', ltd.'":         "Hello World, ltd.",
   "name w/ ws suffix ws":     "Hello    World ltd",
   "name w/ suffix ws":        "Hello World ltd ",
   "name w/ suffix dot ws":    "Hello World ltd. ",
   "name w/ ws suffix dot ws": " Hello World ltd. ",
}

def test_basic_cleanups(terms):
   expected = "Hello World"
   errmsg = "cleanup of %s failed"
   for testname, variation in basic_cleanup_tests.items():
      assert basename(variation, terms) == expected, errmsg % testname

multi_cleanup_tests = {
   "name + suffix":          "Hello World Oy",
   "name + two suffix":      "Hello World Ab Oy",
   "prefix + name":          "Oy Hello World",
   "prefix + name + suffix": "Oy Hello World Ab",
   "name w/ term in middle": "Hello Oy World",
   "name w/ mid + suffix":   "Hello Oy World Ab"
}

def test_multi_type_cleanups(terms):
   expected = "Hello World"
   errmsg = "cleanup of %s failed"
   for testname, variation in multi_cleanup_tests.items():
      result = basename(variation, terms, prefix=True, suffix=True, middle=True)
      assert result == expected, errmsg % testname


# Tests that demonstrate organization name is kept intact

preserving_cleanup_tests = {
   "name with comma": ("Hello, World, ltd.", "Hello, World"),
   "name with dot": ("Hello. World, Oy", "Hello. World")
}

def test_preserving_cleanups(terms):
   errmsg = "preserving cleanup of %s failed"
   for testname, (variation, expected) in preserving_cleanup_tests.items():
      assert basename(variation, terms) == expected, errmsg % testname

# Test umlauts


unicode_umlaut_tests = {
   "name with umlaut in end": ("Säätämö Oy", "Säätämö"),
   "name with umlauts & comma": ("Säätämö, Oy", "Säätämö"),
   "name with no ending umlaut": ("Säätämo Oy", "Säätämo"),
   "name with beginning umlaut": ("Äätämo Oy", "Äätämo"),
   "name with just umlauts": ("Äätämö", "Äätämö"),
   "cyrillic name": ("ОАО Новороссийский морской торговый порт", "Новороссийский морской торговый порт")

}

def test_with_unicode_umlauted_name(terms):
   errmsg = "preserving cleanup of %s failed"
   for testname, (variation, expected) in unicode_umlaut_tests.items():
      assert basename(variation, terms, prefix=True) == expected, errmsg % testname
