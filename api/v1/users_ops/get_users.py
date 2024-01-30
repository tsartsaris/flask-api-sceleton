from flask import Blueprint

from helpers.helpers_s import get_endpoint

create_users_bp = Blueprint('create_users', __name__)


@create_users_bp.route(f'{get_endpoint(__name__)}/get-users', methods=['GET'])
def get_users():
    """
    Retrieves all users.

    This function is mapped to the '/api/v1/users-ops/get-users' path, and responds to HTTP GET requests.

    Returns:
    list: This function currently returns an empty list. It is expected to be updated to return a list of all users.
    """
    all_users = []
    return all_users


@create_users_bp.route(f'{get_endpoint(__name__)}/get-user/<user_id>', methods=['GET'])
def get_user(user_id):
    """
    Retrieves a user based on the provided user_id.

    This function is mapped to the '/api/v1/users-ops/get-user/<user_id>' path, and responds to HTTP GET requests.

    Parameters:
    user_id (str): The ID of the user to be retrieved. This is part of the URL.

    Returns:
    None: This function currently does not return anything. It is expected to be updated to return the requested user.
    """
    print(f"Will get user with id {user_id}")
    return user_id
