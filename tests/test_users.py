import pytest
from flask.testing import FlaskClient


@pytest.mark.webtest
class TestUsersGetRequests:
    def test_no_home(self, client: FlaskClient):
        response = client.get('/')
        assert response.status_code == 404

    def test_users_get(self, client: FlaskClient):
        response = client.get('/api/v1/users-ops/get-users')
        assert response.status_code == 200

    def test_user_get(self, client: FlaskClient):
        response = client.get('/api/v1/users-ops/get-user/1')
        assert response.status_code == 200

    def test_user_get_id(self, client: FlaskClient):
        response = client.get('/api/v1/users-ops/get-user/1')
        assert response.text == "1"
