# Flask API Sceleton for a simple REST API

## Installation

### Create the virtual environment
```bash
python3 -m venv venv
```

### Activate the virtual environment
#### Windows
```bash
venv\Scripts\activate
```

#### Linux
```bash
source venv/bin/activate
```

### Install the requirements
```bash
pip install -r requirements.txt
```

#### Run the application
```bash
python3 main.py
```

#### Run the tests
```bash
pytest -v -k webtest 
```

## Understanding the project structure

The skeleton project structure adheres to a well-organized and modular design, fostering scalability and ease of maintenance in Python development. The main directories include:

- api: Manages the project's API functionality, with version-specific subdirectories (v1) and modules (users_ops).

- app_manager: Handles application setup and initialization, containing modules such as app_setup.

- helpers: Contains utility functions and helper modules. We follow naming conventions such as ending files with _{first letter of developer name} for better in-team communication.

- main.py: The primary file for initiating the project.

- tests: Reserved for testing purposes.

- Configuration files such as pytest.ini and requirements.txt are present at the root. This structured approach enhances code readability, separates concerns, and facilitates collaborative development, enabling contributors to comprehend and extend the project effortlessly.

#### Disclaimer
- This project is for educational purposes only.
- This project is not intended to be used in production as is. 
- This project is not intended to be used in production without proper security review.
- This project is not intended to be used in production without proper testing.
- Some docs generated with Github Copilot :)

