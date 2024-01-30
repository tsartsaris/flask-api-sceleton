from app_manager.app_setup import create_app

# Manage app config settings here and not only     <------------------
# app_config_settings = {
#     'DEBUG': True,
#     'TESTING': False,
#     # ... your settings here
# }
# app = create_app(app_config_settings)


# read from environment variables   <------------------
# import os
# app_config_settings = {
#     'DEBUG': os.environ.get('DEBUG', False),
#     'TESTING': os.environ.get('TESTING', False),
#     # ... your settings here
# }
# app = create_app(app_config_settings)


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
