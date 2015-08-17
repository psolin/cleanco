from cleanco import cleanco


# Tests that demonstrate stuff is stripped away

basic_cleanup_tests = {
   "name with suffix":    "Hello World Oy",
   "name w/ ', ltd.'":    "Hello World, ltd.",
   "name with extra ws":  "Hello    World ltd",
}

def test_basic_cleanups():
   expected = "Hello World"
   errmsg = "cleanup of %s failed"
   for testname, variation in basic_cleanup_tests.items():
      assert cleanco(variation).clean_name() == expected, errmsg % testname


# Tests that demonstrate organization name is kept intact

preserving_cleanup_tests = {
   "name with comma": ("Hello, World, ltd.", "Hello, World"),
   "name with dot": ("Hello. World, Oy", "Hello. World")
}

def test_preserving_cleanups():
   errmsg = "preserving cleanup of %s failed"
   for testname, (variation, expected) in preserving_cleanup_tests.items():
      assert cleanco(variation).clean_name() == expected, errmsg % testname
