import pytest

from app import create_app, db, models

app = create_app(config='config.testing')
app.config['TESTING'] = True


@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            # TODO: init db here
            yield client
            # TODO: drop db here


def test_smoke(client):
    resp = client.get('/')
    print(resp)
