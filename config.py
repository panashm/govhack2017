
import os
basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

# Whoosh does not work on Heroku
WHOOSH_ENABLED = os.environ.get('HEROKU') is None