# FlaskApp

A basic blog application built with flask, based on Corey Schafer's tutorial series on YouTube.

**Environment**
I developed this app in a Python virtual environment, which creates a .venv in the directory.
After creating one, use ``source .venv/bin/activate`` to isolate the application, and ``deactivate`` to turn off the virtual environment.

**Installation:**

In addition to flask, this application uses several dependencies and libraries, including:
- flask_sqlalchemy
- flask_bcrypt
- flask_login
- wtforms
- flask_wtf
- datetime
- os
- secrets
- PIL (pillow)
- email_validator

In order to run the application, use ``pip3 install <library>`` for each dependency (preferrably in a virtual environment) to tie everything together.

**Setup:**
- For each session of use, set ``export FLASK_APP=run.py`` for Mac / Linux or ``set FLASK_APP=run.py`` for Windows.
- From there, type ``flask run`` to start the server.
- By default, the server is not in debug or production mode.

**Behavior**
This app uses ``./blog_app/static/profile_pics`` to store every account's profile pic, and ``./instance`` for database storage. Example instances are there, but different content for each can be made for a separate instance of the site.
