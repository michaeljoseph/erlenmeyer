from flask import json
from mock import Mock, patch
#from peewee import SqliteDatabase
#from playhouse.test_utils import test_database
import requests
from unittest2 import TestCase

from app import app
from cli import an_example_cli


class DrainTestCase(TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        #app.template_folder='erlenmeyer'
        #print(app.template_folder)
        self.app = app.test_client()
        self.app.template_folder = 'erlenmeyer'

        #self.models = [
            #User, Offerer, Bidder,
            #Provider, Manufacturer, Phone,
            #Offer, Contract,
        #]
        #self.test_db = test_database(
            #SqliteDatabase(':memory:'),
            #self.models,
        #)


class ViewTestCase(DrainTestCase):
    def test_index(self):
        result = self.app.get('/')
        self.assertEqual(200, result.status_code)
        self.assertEqual('Hello erlenmeyer!', result.data)


class ModelTestCase(DrainTestCase):
    pass


class ApiTestCase(DrainTestCase):
    def test_publish_endpoint(self):
        response = self.app.get('/api')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(
            json.loads(response.data),
            app.config['API_RESPONSE']
        )


class CliTestCase(DrainTestCase):
    def setUp(self):
        super(CliTestCase, self).setUp()
        self.requests_patcher = patch('erlenmeyer.cli.requests')
        self.requests = self.requests_patcher.start()
        self.response = Mock(spec=requests.Response, status_code=200)

        for method in ('get', 'post', 'put', 'patch', 'delete'):
            fn = getattr(self.requests, method)
            fn.return_value = self.response

    def tearDown(self):
        self.requests_patcher.stop()

    def test_an_example_cli(self):
        an_example_cli('an-identifier')
        self.requests.get.assert_called_with(
            app.config['EXTERNAL_API_URL'],
            params={'ident': 'an-identifier'},
        )
