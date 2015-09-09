# encoding: utf-8

from cleanco import cleanco


# Tests that demonstrate stuff is stripped away

basic_cleanup_tests = {
   "name w/ suffix":           "Hello World Oy",
   "name w/ ', ltd.'":         "Hello World, ltd.",
   "name w/ ws suffix ws":     "Hello    World ltd",
   "name w/ suffix ws":        "Hello World ltd ",
   "name w/ suffix dot ws":    "Hello World ltd. ",
   "name w/ ws suffix dot ws": " Hello World ltd. ",
}

def test_basic_cleanups():
   expected = "Hello World"
   errmsg = "cleanup of %s failed"
   for testname, variation in basic_cleanup_tests.items():
      assert cleanco(variation).clean_name() == expected, errmsg % testname

multi_cleanup_tests = {
   "name + suffix":          "Hello World Oy",
   "name + two suffix":      "Hello World Ab Oy",
   "prefix + name":          "Oy Hello World",
   "prefix + name + suffix": "Oy Hello World Ab",
   "name w/ term in middle": "Hello Oy World",
   "name w/ mid + suffix":   "Hello Oy World Ab"
}

def test_multi_type_cleanups():
   expected = "Hello World"
   errmsg = "cleanup of %s failed"
   for testname, variation in multi_cleanup_tests.items():
      result = cleanco(variation).clean_name(prefix=True, suffix=True, middle=True, multi=True)
      assert result == expected, errmsg % testname


# Tests that demonstrate organization name is kept intact

preserving_cleanup_tests = {
   "name with comma": (u"Hello, World, ltd.", u"Hello, World"),
   "name with dot": (u"Hello. World, Oy", u"Hello. World")
}

def test_preserving_cleanups():
   errmsg = "preserving cleanup of %s failed"
   for testname, (variation, expected) in preserving_cleanup_tests.items():
      assert cleanco(variation).clean_name() == expected, errmsg % testname

# Test umlauts


unicode_umlaut_tests = {
   "name with umlaut in end": (u"Säätämö Oy", u"Säätämö"),
   "name with umlauts & comma": (u"Säätämö, Oy", u"Säätämö"),
   "name with no ending umlaut": (u"Säätämo Oy", u"Säätämo"),
   "name with beginning umlaut": (u"Äätämo Oy", u"Äätämo"),
   "name with just umlauts": (u"Äätämö", u"Äätämö")
}

def test_with_unicode_umlauted_name():
   errmsg = "preserving cleanup of %s failed"
   for testname, (variation, expected) in unicode_umlaut_tests.items():
      assert cleanco(variation).clean_name() == expected, errmsg % testname
