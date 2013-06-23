from extension import Erlenmeyer
from flask import Flask

import settings

app = Flask('drain')
erlenmeyer = Erlenmeyer(app, settings)
database = erlenmeyer.database
toolbar = erlenmeyer.toolbar

import views
import api
hush_pyflakes = (views, api)
