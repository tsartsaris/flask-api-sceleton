from flask import Flask

from api.v1.users_ops.get_users import create_users_bp


def create_app(settings_overrides=None):
    """
    This function creates a Flask application and configures it with the given settings and blueprints.

    Parameters:
    settings_overrides (dict, optional): A dictionary of settings that should override the default settings.
                                         If None, the default settings are used.

    Returns:
    app (Flask): The created and configured Flask application.

    Example:
    If the input is {"DEBUG": False}, the function will create a Flask application with DEBUG set to False.
    """

    app = Flask(__name__)
    configure_settings(app, settings_overrides)
    configure_blueprints(app)
    return app


def configure_settings(app, settings_override):
    """
    This function configures the settings of the Flask application.

    Parameters:
    app (Flask): The Flask application to be configured.
    settings_override (dict, optional): A dictionary of settings that should override the default settings.
                                        If None, the default settings are used.

    Returns:
    None
    """

    app.config.update({
        'DEBUG': True,
        'TESTING': False,
        # constant settings that will not be passed with settings_override
    })
    if settings_override:
        app.config.update(settings_override)


def configure_blueprints(app):
    """
    This function configures the blueprints of the Flask application.

    Parameters:
    app (Flask): The Flask application to be configured.

    Returns:
    None
    """

    app.register_blueprint(create_users_bp)
    print(app.url_map)  # print the url map of the app to the console for debugging purposes
