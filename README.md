# FlaskApp

A basic blog application built with flask, based on Corey Schafer's tutorial series.

**Installation:**

In addition to flask, this application uses several dependencies and libraries, including:
- sqlalchemy
- bcrypt
- login
- wtforms
- datetime

In order to run the application, use ``pip install <library>`` for each dependency (preferrably in a virtual environment) to tie everything together.

**Setup:**
- After creating a Python virtual environment, use ``source .venv/bin/activate`` to isolate the application.
- For first time use, set ``export FLASK_APP=run.py`` for Mac / Linux or ``set FLASK_APP=run.py`` for Windows.
- For any subsequent use, type ``flask run`` to start the server.
- By default, the server is not in debug or production mode.
