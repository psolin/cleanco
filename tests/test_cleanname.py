# encoding: utf-8
"""
Comprehensive test suite for cleanco business name cleaning functionality.

Test Categories:
1. Core Functionality Tests
2. Edge Case Tests
3. Unicode and Internationalization Tests
"""

import pytest
from cleanco import basename


# ============================================================================
# 1. CORE FUNCTIONALITY TESTS
# ============================================================================

def test_deterministic_terms(monkeypatch):
    """
    1.1 Test deterministic term preparation

    Ensures prepare_default_terms() returns consistent results regardless
    of the ordering of terms returned by get_unique_terms().
    """
    from cleanco import clean
    with monkeypatch.context() as m:
        mock_terms = ["aaa", "bbb", "ccc"]
        m.setattr(clean, "get_unique_terms", lambda: mock_terms)
        res1 = clean.prepare_default_terms()
        m.setattr(clean, "get_unique_terms", lambda: reversed(mock_terms))
        res2 = clean.prepare_default_terms()
        assert res1 == res2


basic_cleanup_tests = {
    "name w/ suffix":           "Hello World Oy",
    "name w/ ', ltd.'":         "Hello World, ltd.",
    "name w/ ws suffix ws":     "Hello    World ltd",
    "name w/ suffix ws":        "Hello World ltd ",
    "name w/ suffix dot ws":    "Hello World ltd. ",
    "name w/ ws suffix dot ws": " Hello World ltd. ",
}

def test_basic_cleanups():
    """
    1.2 Test basic suffix removal

    Tests that common legal suffixes are properly identified and removed
    with various whitespace and punctuation configurations.

    Sub-tests:
    1.2.1 - Simple suffix removal
    1.2.2 - Suffix with comma before
    1.2.3 - Multiple whitespace handling
    1.2.4 - Trailing whitespace handling
    1.2.5 - Suffix with period and trailing space
    1.2.6 - Leading and trailing whitespace
    """
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
    """
    1.3 Test prefix, suffix, and middle term removal

    Tests removal of legal terms from various positions when
    prefix=True, suffix=True, and middle=True are enabled.

    Sub-tests:
    1.3.1 - Suffix-only removal
    1.3.2 - Suffix without punctuation
    1.3.3 - Prefix-only removal
    1.3.4 - Prefix and suffix removal
    1.3.5 - Middle term removal
    1.3.6 - Complex middle term removal (compound terms)
    1.3.7 - Middle and suffix removal
    """
    expected = "Hello World"
    errmsg = "cleanup of %s failed"
    for testname, variation in multi_cleanup_tests.items():
        result = basename(variation, prefix=True, suffix=True, middle=True)
        assert result == expected, errmsg % testname


double_cleanup_tests = {
    "name + two prefix":      "Ab Oy Hello World",
    "name + two suffix":      "Hello World Ab Oy",
    "name + two in middle":   "Hello Ab Oy World"
}

def test_double_cleanups():
    """
    1.4 Test iterative cleaning (running basename twice)

    Verifies that running basename() multiple times can remove
    multiple legal terms that weren't caught in a single pass.

    Sub-tests:
    1.4.1 - Two prefixes requiring double pass
    1.4.2 - Two suffixes requiring double pass
    1.4.3 - Two middle terms requiring double pass
    """
    expected = "Hello World"
    errmsg = "cleanup of %s failed"
    for testname, variation in multi_cleanup_tests.items():
        result = basename(variation, prefix=True, suffix=True, middle=True)
        final = basename(result, prefix=True, suffix=True, middle=True)
        assert final == expected, errmsg % testname


preserving_cleanup_tests = {
    "name with comma": ("Hello, World, ltd.", "Hello, World"),
    "name with dot": ("Hello. World, Oy", "Hello. World")
}

def test_preserving_cleanups():
    """
    1.5 Test punctuation preservation in company names

    Ensures that punctuation that is part of the actual company name
    (commas, periods) is preserved while legal suffixes are removed.

    Sub-tests:
    1.5.1 - Comma in company name preserved
    1.5.2 - Period in company name preserved
    """
    errmsg = "preserving cleanup of %s failed"
    for testname, (variation, expected) in preserving_cleanup_tests.items():
        assert basename(variation) == expected, errmsg % testname


unicode_umlaut_tests = {
    "name with umlaut in end": ("Säätämö Oy", "Säätämö"),
    "name with umlauts & comma": ("Säätämö, Oy", "Säätämö"),
    "name with no ending umlaut": ("Säätämo Oy", "Säätämo"),
    "name with beginning umlaut": ("Äätämo Oy", "Äätämo"),
    "name with just umlauts": ("Äätämö", "Äätämö"),
    "cyrillic name": ("ОАО Новороссийский морской торговый порт", "Новороссийский морской торговый порт")
}

def test_with_unicode_umlauted_name():
    """
    1.6 Test Finnish/Nordic umlaut handling

    Tests that company names with Nordic umlauts (ä, ö) and Cyrillic
    characters are handled correctly with prefix removal.

    Sub-tests:
    1.6.1 - Umlaut at end of name
    1.6.2 - Umlauts with comma punctuation
    1.6.3 - Umlaut in middle of name
    1.6.4 - Umlaut at beginning of name
    1.6.5 - Name consisting only of umlauts
    1.6.6 - Cyrillic script with prefix removal
    """
    errmsg = "preserving cleanup of %s failed"
    for testname, (variation, expected) in unicode_umlaut_tests.items():
        assert basename(variation, prefix=True) == expected, errmsg % testname


terms_with_accents_tests = {
    "term with ł correct spelling": ("Łoś spółka z o.o", "Łoś"),
    "term with ł incorrect spelling": ("Łoś spolka z o.o", "Łoś"),
}

def test_terms_with_accents():
    """
    1.7 Test Polish accented term matching

    Verifies that Polish legal terms with special characters (ł, ó)
    are correctly matched and removed, with normalization handling
    different spellings.

    Sub-tests:
    1.7.1 - Correctly spelled Polish term (spółka)
    1.7.2 - Normalized spelling without accents (spolka)
    """
    errmsg = "preserving cleanup of %s failed"
    for testname, (variation, expected) in terms_with_accents_tests.items():
        assert basename(variation, suffix=True) == expected, errmsg % testname


# ============================================================================
# 2. EDGE CASE TESTS
# ============================================================================

empty_result_single_tests = {
    "AMBA (Danish term)": "AMBA",
    "Inc": "Inc",
    "LLC": "LLC",
    "Ltd": "Ltd",
    "Corporation": "Corporation",
    "Limited": "Limited",
}

def test_empty_result_single_terms():
    """
    2.1 Test empty results from single legal terms

    Documents current behavior: when input consists only of a single
    legal term, the result is an empty string.

    Sub-tests:
    2.1.1 - AMBA (Danish term)
    2.1.2 - Inc
    2.1.3 - LLC
    2.1.4 - Ltd
    2.1.5 - Corporation
    2.1.6 - Limited
    """
    expected = ''
    errmsg = "empty result test for %s failed"
    for testname, variation in empty_result_single_tests.items():
        assert basename(variation) == expected, errmsg % testname


empty_result_multiple_tests = {
    "inc & co": "inc & co",
    "Ltd. & Co.": "Ltd. & Co.",
}

def test_empty_result_multiple_terms():
    """
    2.2 Test empty results from multiple legal terms

    When input consists only of multiple legal terms, result is empty.
    This edge case is related to test 2.1.

    Sub-tests:
    2.2.1 - "inc & co" returns empty
    2.2.2 - "Ltd. & Co." returns empty
    """
    expected = ''
    errmsg = "empty result test for %s failed"
    for testname, variation in empty_result_multiple_tests.items():
        assert basename(variation) == expected, errmsg % testname


punctuation_handling_tests = {
    "ampersand (&) preservation": ("Smith & Jones Corporation", "Smith & Jones"),
    "hyphen (-) preservation": ("Smith-Jones Ltd", "Smith-Jones"),
    "apostrophe (') preservation": ("McDonald's Corporation", "McDonald's"),
    "multiple periods (abbreviations)": ("A.B.C. Corp", "A.B.C."),
    "trailing exclamation removal": ("Yahoo! Inc", "Yahoo"),
}

def test_punctuation_handling():
    """
    2.3 Test various punctuation scenarios

    Tests how different punctuation marks are handled in company names.

    Sub-tests:
    2.3.1 - Ampersand (&) preservation
    2.3.2 - Hyphen (-) preservation
    2.3.3 - Apostrophe (') preservation
    2.3.4 - Multiple periods (abbreviations)
    2.3.5 - Trailing exclamation marks removal

    Note: Test 2.3.5 documents current behavior where trailing exclamation
    marks are removed (e.g., "Yahoo! Inc" becomes "Yahoo"). This is inconsistent
    with the preservation of other punctuation marks like apostrophes and
    ampersands, and may be addressed in a future update.
    """
    errmsg = "punctuation handling test for %s failed"
    for testname, (variation, expected) in punctuation_handling_tests.items():
        assert basename(variation) == expected, errmsg % testname


case_insensitivity_tests = {
    "uppercase term (LLC)": ("Company Name LLC", "Company Name"),
    "lowercase term (llc)": ("Company Name llc", "Company Name"),
    "mixed case term (LlC)": ("Company Name LlC", "Company Name"),
}

def test_case_insensitivity():
    """
    2.4 Test case-insensitive term matching

    Verifies that legal terms are matched regardless of case (uppercase,
    lowercase, or mixed case).

    Sub-tests:
    2.4.1 - Uppercase term (LLC)
    2.4.2 - Lowercase term (llc)
    2.4.3 - Mixed case term (LlC)
    """
    errmsg = "case insensitivity test for %s failed"
    for testname, (variation, expected) in case_insensitivity_tests.items():
        assert basename(variation) == expected, errmsg % testname


compound_terms_tests = {
    "Pty Ltd compound": ("Example Company Pty Ltd", "Example"),
    "Pty Limited (known issue)": ("Example Example Pty Limited", "Example Example Pty"),
    "entire name is legal terms": ("Company Pvt. Ltd.", ""),
}

def test_compound_terms():
    """
    2.5 Test compound legal terms

    Tests handling of multi-word legal designations and documents
    known issues.

    Sub-tests:
    2.5.1 - "Pty Ltd" compound (note: 'Company' also removed as it's a term)
    2.5.2 - "Pty Limited" known bug - doesn't work correctly
    2.5.3 - "Pvt. Ltd." where entire name is legal terms
    """
    errmsg = "compound terms test for %s failed"
    for testname, (variation, expected) in compound_terms_tests.items():
        assert basename(variation) == expected, errmsg % testname


real_world_companies_tests = {
    "Apple Inc.": ("Apple Inc.", "Apple"),
    "Microsoft Corporation": ("Microsoft Corporation", "Microsoft"),
    "Berkshire Hathaway Inc.": ("Berkshire Hathaway Inc.", "Berkshire Hathaway"),
    "Procter & Gamble Co.": ("Procter & Gamble Co.", "Procter & Gamble"),
    "AT&T Inc.": ("AT&T Inc.", "AT&T"),
}

def test_real_world_companies():
    """
    2.6 Test real-world company names

    Tests with actual well-known company names to ensure practical
    applicability.

    Sub-tests:
    2.6.1 - Apple Inc.
    2.6.2 - Microsoft Corporation
    2.6.3 - Berkshire Hathaway Inc.
    2.6.4 - Procter & Gamble Co.
    2.6.5 - AT&T Inc.
    """
    errmsg = "real world company test for %s failed"
    for testname, (variation, expected) in real_world_companies_tests.items():
        assert basename(variation) == expected, errmsg % testname


numbers_in_names_tests = {
    "numbers after name": ("Company 123 Ltd", "Company 123"),
    "name only numbers": ("123456 Inc", "123456"),
    "mixed alphanumeric": ("ABC123 Corporation", "ABC123"),
}

def test_numbers_in_names():
    """
    2.7 Test company names containing numbers

    Verifies that numeric characters in company names are preserved.

    Sub-tests:
    2.7.1 - Numbers after name
    2.7.2 - Name consisting only of numbers
    2.7.3 - Mixed alphanumeric name
    """
    errmsg = "numbers in names test for %s failed"
    for testname, (variation, expected) in numbers_in_names_tests.items():
        assert basename(variation) == expected, errmsg % testname


special_formats_tests = {
    "all uppercase": ("IBM CORPORATION", "IBM"),
    "periods as abbreviations": ("U.S. Steel Corp.", "U.S. Steel"),
    "single letter name": ("X Corporation", "X"),
}

def test_special_formats():
    """
    2.8 Test special formatting scenarios

    Tests edge cases with unusual formatting patterns.

    Sub-tests:
    2.8.1 - All uppercase company name
    2.8.2 - Periods used as abbreviations
    2.8.3 - Single letter company name
    """
    errmsg = "special formats test for %s failed"
    for testname, (variation, expected) in special_formats_tests.items():
        assert basename(variation) == expected, errmsg % testname


whitespace_handling_tests = {
    "leading whitespace": ("  Hello World Ltd", "Hello World"),
    "trailing whitespace": ("Hello World Ltd  ", "Hello World"),
    "whitespace around term only": ("  LLC  ", ""),
}

def test_whitespace_handling():
    """
    2.9 Test whitespace handling

    Verifies that leading and trailing whitespace is properly handled.

    Sub-tests:
    2.9.1 - Leading whitespace
    2.9.2 - Trailing whitespace
    2.9.3 - Whitespace around legal term only
    """
    errmsg = "whitespace handling test for %s failed"
    for testname, (variation, expected) in whitespace_handling_tests.items():
        assert basename(variation) == expected, errmsg % testname


ambiguous_term_tests = {
    "Limited in name and suffix": ("Limited Edition Products Ltd", "Limited Edition Products"),
}

def test_ambiguous_term_in_name():
    """
    2.10 Test ambiguous cases where legal term appears in actual name

    When a legal term like "Limited" appears as part of the actual
    company name, only suffix occurrences should be removed.

    Example: "Limited Edition Products Ltd" should become
    "Limited Edition Products" not "Edition Products"
    """
    errmsg = "ambiguous term test for %s failed"
    for testname, (variation, expected) in ambiguous_term_tests.items():
        assert basename(variation) == expected, errmsg % testname


# ============================================================================
# 3. UNICODE AND INTERNATIONALIZATION TESTS
# ============================================================================

unicode_non_latin_scripts_tests = {
    "Arabic script": ('شركة المثال المحدودة', 'شركة المثال المحدودة'),
    "Hebrew script": ('חברה בע״מ', 'חברה בע״מ'),
    "Japanese (Kanji + Hiragana)": ('株式会社サンプル', '株式会社サンプル'),
    "Korean (Hangul)": ('삼성전자 주식회사', '삼성전자 주식회사'),
    "Thai script": ('บริษัท จำกัด', 'บริษัท จำกัด'),
    "Greek alphabet": ('Εταιρεία Περιορισμένης Ευθύνης', 'Εταιρεία Περιορισμένης Ευθύνης'),
    "Chinese with English suffix": ('北京公司 Ltd', '北京公司'),
    "Cyrillic with English suffix": ('Москва Corporation', 'Москва'),
    "Japanese with English suffix": ('東京株式会社 Inc.', '東京株式会社'),
}

def test_unicode_non_latin_scripts():
    """
    3.1 Test various Unicode and non-Latin scripts

    Tests that the library handles non-Latin scripts correctly,
    preserving them when they don't match legal terms.

    Sub-tests:
    3.1.1 - Arabic script
    3.1.2 - Hebrew script
    3.1.3 - Japanese (Kanji + Hiragana)
    3.1.4 - Korean (Hangul)
    3.1.5 - Thai script
    3.1.6 - Greek alphabet
    3.1.7 - Chinese with English suffix
    3.1.8 - Cyrillic with English suffix
    3.1.9 - Japanese with English suffix
    """
    errmsg = "unicode non-Latin script test for %s failed"
    for testname, (variation, expected) in unicode_non_latin_scripts_tests.items():
        assert basename(variation) == expected, errmsg % testname


unicode_special_characters_tests = {
    "French accents": ('Société Française Ltd', 'Société Française'),
    "Spanish accents": ('Compañía Española S.A.', 'Compañía Española'),
    "Portuguese abbreviation": ('Empresa Ltda.', 'Empresa'),
    "German umlauts (Müller & Söhne)": ('Müller & Söhne GmbH', 'Müller & Söhne'),
    "German umlauts in name": ('Schöne Bücher Ltd', 'Schöne Bücher'),
    "Nordic Ø character": ('Ørsted A/S', 'Ørsted'),
    "Nordic Å character": ('Åland Corporation', 'Åland'),
    "Czech characters": ('Český Krumlov s.r.o.', 'Český Krumlov'),
    "Polish Ł character": ('Łódź Spółka', 'Łódź Spółka'),
}

def test_unicode_special_characters():
    """
    3.2 Test Unicode special characters and accented Latin scripts

    Tests handling of Latin script with diacritical marks and special
    characters from various European languages.

    Sub-tests:
    3.2.1 - French accents (Société)
    3.2.2 - Spanish accents (Compañía)
    3.2.3 - Portuguese abbreviation (Ltda.)
    3.2.4 - German umlauts (Müller, Söhne)
    3.2.5 - German umlauts in name (Schöne Bücher)
    3.2.6 - Nordic Ø character
    3.2.7 - Nordic Å character
    3.2.8 - Czech characters (Český)
    3.2.9 - Polish Ł character
    """
    errmsg = "unicode special characters test for %s failed"
    for testname, (variation, expected) in unicode_special_characters_tests.items():
        assert basename(variation) == expected, errmsg % testname


unicode_mixed_content_tests = {
    "mathematical symbol": ('Alpha β Gamma Corp', 'Alpha β Gamma'),
    "currency symbol": ('€uro Company Ltd', '€uro Company'),
    "combining characters": ('Naïve Café Inc.', 'Naïve Café'),
}

def test_unicode_mixed_content():
    """
    3.3 Test mixed Unicode content with special symbols

    Tests handling of Unicode content that includes emojis, mathematical
    symbols, currency symbols, and combining characters.

    Sub-tests:
    3.3.1 - Emoji in company name
    3.3.2 - Greek letter (mathematical symbol)
    3.3.3 - Currency symbol (Euro)
    3.3.4 - Combining diacritical marks (ï, é)
    """
    # Emoji test handled separately due to different assertion style
    result = basename('Tech 🚀 Innovation Ltd')
    assert 'Tech' in result and 'Innovation' in result, "emoji test failed"

    errmsg = "unicode mixed content test for %s failed"
    for testname, (variation, expected) in unicode_mixed_content_tests.items():
        assert basename(variation) == expected, errmsg % testname


unicode_right_to_left_tests = {
    "Arabic with English suffix": ('الشركة العربية Ltd', 'الشركة العربية'),
    "Hebrew with English suffix": ('החברה העברית Inc.', 'החברה העברית'),
}

def test_unicode_right_to_left():
    """
    3.4 Test right-to-left (RTL) script handling

    Tests that RTL scripts (Arabic, Hebrew) are correctly preserved
    when combined with LTR English legal suffixes.

    Sub-tests:
    3.4.1 - Arabic with English suffix
    3.4.2 - Hebrew with English suffix
    """
    errmsg = "unicode RTL script test for %s failed"
    for testname, (variation, expected) in unicode_right_to_left_tests.items():
        result = basename(variation)
        assert expected in result, errmsg % testname


unicode_normalization_tests = {
    "composed form (single char)": ('Café Ltd', 'Café'),
    "decomposed form (base + combining)": ('Café Ltd', 'Café'),
}

def test_unicode_normalization():
    """
    3.5 Test Unicode normalization handling

    Tests that different Unicode representations of the same visual
    character (composed vs decomposed forms) are handled consistently.

    For example, é can be represented as:
    - Single character U+00E9 (composed form)
    - Two characters U+0065 + U+0301 (e + combining acute accent)

    Both should be normalized and treated equivalently.

    Sub-tests:
    3.5.1 - Composed form (single character)
    3.5.2 - Decomposed form (base + combining character)
    """
    errmsg = "unicode normalization test for %s failed"
    for testname, (variation, expected_contains) in unicode_normalization_tests.items():
        result = basename(variation)
        assert 'Caf' in result, errmsg % testname
