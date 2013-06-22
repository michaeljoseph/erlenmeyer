from extension import Erlenmeyer
from flask import Flask

import settings

app = Flask('drain')
database = Erlenmeyer(app, settings).database

import views
import api
hush_pyflakes = (views, api)
