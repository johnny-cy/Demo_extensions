from demo_app import app, create_app
import pytest


flask_app = create_app()

@pytest.fixture()
def test_client():
    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client 

# next, the apllication context has already pushed onto the stack for use by the test functions.
def test_getname(test_client):
    res = test_client.get("/getName")
    assert 200 == res.status_code
