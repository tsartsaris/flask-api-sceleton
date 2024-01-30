import pytest
from flask.testing import FlaskClient


@pytest.mark.webtest
class TestUsersGetRequests:
    """
    This class contains tests for GET requests to the Users API.

    It uses the pytest framework and the FlaskClient for making requests to the API.
    """

    def test_no_home(self, client: FlaskClient):
        """
        Test for the home route.

        This test checks if a GET request to the home route returns a 404 status code.

        Args:
            client (FlaskClient): The Flask test client.

        Returns:
            None
        """
        response = client.get('/')
        assert response.status_code == 404

    def test_users_get(self, client: FlaskClient):
        """
        Test for the get-users route.

        This test checks if a GET request to the get-users route returns a 200 status code.

        Args:
            client (FlaskClient): The Flask test client.

        Returns:
            None
        """
        response = client.get('/api/v1/users-ops/get-users')
        assert response.status_code == 200

    def test_user_get(self, client: FlaskClient):
        """
        Test for the get-user route with a specific user ID.

        This test checks if a GET request to the get-user route with a specific user ID returns a 200 status code.

        Args:
            client (FlaskClient): The Flask test client.

        Returns:
            None
        """
        response = client.get('/api/v1/users-ops/get-user/1')
        assert response.status_code == 200

    def test_user_get_id(self, client: FlaskClient):
        """
        Test for the get-user route with a specific user ID.

        This test checks if a GET request to the get-user route with a specific user ID returns the correct user ID in the response text.

        Args:
            client (FlaskClient): The Flask test client.

        Returns:
            None
        """
        response = client.get('/api/v1/users-ops/get-user/1')
        assert response.text == "1"
