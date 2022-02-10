from week5team_names import make_full_name, \
    extract_given_name, extract_family_name
import pytest

def test_make_full_name():
    assert make_full_name("Innocent", "Hove") == "Hove; Innocent"
    assert make_full_name("Higor", "Costa") == "Costa; Higor"
    assert make_full_name("Mitchelle", "Garrett") == "Garrett; Mitchelle"
    assert make_full_name("Manuel", "Gueverra") == "Gueverra; Manuel"
    assert make_full_name("Jairo", "Tinoco") == "Tinoco; Jairo"

def test_extract_given_name():
    assert extract_given_name("Hove; Innocent") == "Innocent"
    assert extract_given_name("Costa; Higor") == "Higor"
    assert extract_given_name("Garrett; Mitchelle") == "Mitchelle"
    assert extract_given_name("Gueverra; Manuel") == "Manuel"
    assert extract_given_name("Tinoco; Jairo") == "Jairo"

def test_extract_family_name():
    assert extract_family_name("Hove; Innocent") == "Hove"
    assert extract_family_name("Costa; Higor") == "Costa"
    assert extract_family_name("Garrett; Mitchelle") == "Garrett"
    assert extract_family_name("Gueverra; Manuel") == "Gueverra"
    assert extract_family_name("Tinoco; Jairo") == "Tinoco"

# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", "week5team_test_names.py"])

# from names import make_full_name, extract_given_name, extract_family_name
# import pytest

# def test_make_full_name():
#     """Verify that the make_full_name function returns correct results."""
#     assert make_full_name("Penelope", "Smith-Jones") == "Smith-Jones; Penelope"
#     assert make_full_name("George", "Washington") == "Washington; George"
#     assert make_full_name("J", "Ng") == "Ng; J"
#     assert make_full_name("", "") == "; "

# def test_extract_family_name():
#     """Verify that the extract_family_name function returns correct results."""
#     assert extract_family_name("Smith-Jones; Penelope") == "Smith-Jones"
#     assert extract_family_name("Washington; George") == "Washington"
#     assert extract_family_name("Ng; J") == "Ng"
#     assert extract_family_name("; ") == ""

# def test_extract_given_name():
#     """Verify that the extract_given_name function returns correct results."""
#     assert extract_given_name("Smith-Jones; Penelope") == "Penelope"
#     assert extract_given_name("Washington; George") == "George"
#     assert extract_given_name("Ng; J") == "J"
#     assert extract_given_name("; ") == ""

# # Call the main function that is part of pytest so that
# # the test functions in this file will start executing.
# pytest.main(["-v", "--tb=line", "-rN", "test_names.py"])