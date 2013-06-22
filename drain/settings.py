DEBUG = True
SECRET_KEY = 'ssshhhh'

# application config
API_RESPONSE = {'message': 'All good'}
EXTERNAL_API_URL = 'http://httpbin.org/get'
SENTRY_DSN = ''

# logging
LOG_FILE = 'drain.log'
LOG_LEVEL = 'INFO'
LOG_FORMAT = (
    '%(levelname)s %(asctime)s '
    '%(module)s %(process)d '
    '%(thread)d %(message)s'
)

# database
DATABASE_ENGINE = 'peewee.SqliteDatabase'
DATABASE_NAME = 'drain.db'
DATABASE = {
    'name': DATABASE_NAME,
    'engine': DATABASE_ENGINE
}
