# tdd_converter_app
Short converter app with TDD approach

Tutorial followed in this [medium page](https://medium.com/the-andela-way/test-driven-development-with-django-ccb179171dcd).

This version, however, is working for Django 2.1.7 and Python 3.7. Tutorial version of the app makes a couple mistakes corrected in this version.

## Startup
Run the following command inside the **converter** folder
```terminal
python manage.py runserver
```
which will run in `http://localhost:8000` by default. To go  into the converter app, simply navigate to `/length/convert/`

## Tests
To run the written tests for the converter app run the following command
```terminal
python manage.py test
```
Output should read something similar to this
```terminal
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
....
----------------------------------------------------------------------
Ran 4 tests in 0.023s

OK
Destroying test database for alias 'default'...
```
