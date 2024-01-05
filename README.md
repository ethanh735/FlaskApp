# FlaskApp

A basic blog application built with flask, based on Corey Schafer's tutorial series on YouTube.

**Environment:**\
I developed this app in a Python virtual environment, which creates a .venv in the directory.
After creating one, use ``source .venv/bin/activate`` to isolate the application, and ``deactivate`` to turn off the virtual environment.

I also have the application's most important variables, such as ``SECRET_KEY`` and ``FLASK_APP``, to my .bash_profile config file so that security-sensitive data is not hard-coded, others can generate different values for their own uses, and runtime is smoother due to things being already set up.

**Installation:**\
In addition to flask, this application uses several dependencies and libraries, which are included in the ``requirements.txt`` file. Feel free to read through and\or update them as necessary.

To install the packages in the file, simply type ``pip3 install -r requirements.txt`` on the command line.

**Setup:**
- Type ``flask run`` to start the server.
- By default, the server is not in debug or production mode.

**Behavior:**\
This app uses ``./blog_app/static/profile_pics`` to store every account's profile pic, and ``./instance`` for database storage. Example instances are there, but different content for each can be made for a separate instance of the site.
