# erlenmeyer: a big flask full of opinionated batteries

## Features

* Configuration
* Logging
* API (simple)
* CLI (with [docopt](http://dotopt.org))
* Templates (todo)
  * [bootstrap](http://twitter.github.io/bootstrap/)
  * https://github.com/mbr/flask-bootstrap
  * http://rriepe.github.io/1pxdeep/
  * [bootswatch](http://bootswatch.com/)

* Persistence
  * [peewee](https://github.com/coleifer/peewee)
  * [flask-peewee](https://github.com/coleifer/flask-peewee)
  * https://github.com/guilhermechapiewski/simple-db-migrate
    - sqlite patch
    - peewee patch
    - match migrations by number / substring

* [SQLite]
  * http://www.sqlite.org/draft/wal.html
  * http://stackoverflow.com/questions/913067/sqlite-as-a-production-database-for-a-low-traffic-site

* [flask-peewee](https://github.com/coleifer/flask-peewee)
* User auth
  * https://github.com/mattupstate/flask-social
  * http://pythonhosted.org/Flask-Security/quickstart.html
* Procfile
  * https://github.com/kennethreitz/flask-heroku/
* Celery
  * http://flask.pocoo.org/docs/patterns/celery/
* Sentry (link)

## Usage

Have a look at the [example project]()

## Development

    # clone the repo
    # virtualenv, install requirements
    # nosetests

## TODO

* pinned requirements in setup, relative requirements in requirements.txt
* statsd
* new relic
* google analytics
* complete testing story
* pedantic
  * Linting
  * Testing (http://peewee.readthedocs.org/en/latest/peewee/playhouse.html#test-utils)
  * Sphinx docs
* database migrations
* API: flask-peewee, flask model views
