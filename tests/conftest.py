import json
import functools
import os
import sys

import pytest
from flask import Flask

# Set up the path to import from `modules`.
root = os.path.join(os.path.dirname(__file__))
package = os.path.join(root, '..')
sys.path.insert(0, os.path.abspath(package))

from app_manager.app_setup import create_app


def humanize_werkzeug_client(client_method):
    """
    Wraps a `werkzeug` client method (the client provided by `Flask`) to make
    it easier to use in tests.

    Args:
        client_method (function): The client method to be wrapped.

    Returns:
        function: The wrapped client method.
    """

    @functools.wraps(client_method)
    def wrapper(url, **kwargs):
        """
        The wrapper function for the client method.

        Args:
            url (str): The URL to be accessed by the client method.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: The response from the client method.
        """
        # Always set the content type to `application/json`.
        kwargs.setdefault('headers', {}).update({
            'content-type': 'application/json'
        })

        # If data is present then make sure it is json encoded.
        if 'data' in kwargs:
            data = kwargs['data']
            if isinstance(data, dict):
                kwargs['data'] = json.dumps(data)

        kwargs['buffered'] = True

        return client_method(url, **kwargs)

    return wrapper


@pytest.fixture(scope='session', autouse=True)
def app(request):
    """
    Pytest fixture for creating a Flask app with TESTING configuration.

    Args:
        request (FixtureRequest): The pytest request object.

    Returns:
        Flask: The created Flask app.
    """
    app = create_app({
        'TESTING': True
    })

    # Establish an application context before running the tests.
    ctx = app.app_context()
    ctx.push()

    def teardown():
        """
        Teardown function to be called after the test session.
        """
        ctx.pop()

    request.addfinalizer(teardown)
    return app


@pytest.fixture(scope='function')
def client(app, request):
    """
    Pytest fixture for creating a Flask test client.

    Args:
        app (Flask): The Flask app.
        request (FixtureRequest): The pytest request object.

    Returns:
        FlaskClient: The created Flask test client.
    """
    return app.test_client()


@pytest.fixture(scope='function')
def get(client):
    """
    Pytest fixture for creating a humanized GET method for the Flask test client.

    Args:
        client (FlaskClient): The Flask test client.

    Returns:
        function: The humanized GET method.
    """
    return humanize_werkzeug_client(client.get)
