"""
put fixture in conftest.py if multiple pyfile gonna use

filename 'conftest' shouldn't be changed.

required __init__.py in the same dir.
"""

import pytest

@pytest.fixture()
def fixture_setup_from_conftest():
    print("fixture setup..")
    name = "John"
    yield name
    name = ""
