"""
8. fixture can be set both from conftest and inside module
9. fixture in module will be firstly used if there are names in same.

"""
import pytest

@pytest.fixture()
def fixture_setup_in_module():
    print("fixture setup in module..")
    name = "Mike"
    yield name
    name = ""


def test2(fixture_setup_from_conftest):
    assert fixture_setup_from_conftest == "John"

def test1(fixture_setup_in_module):
    assert fixture_setup_in_module == "Mike"