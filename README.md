# erlenmeyer: a big flask full of opinionated batteries

## Features

* Configuration
* Logging
* API (simple)
* CLI (with [docopt](http://dotopt.org))
  * http://flask-script.readthedocs.org/en/latest/
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

* Admin interface (fllask-peewee, 

http://elsdoerfer.name/docs/flask-assets/
http://pythonhosted.org/Flask-Cache/
http://sjl.bitbucket.org/flask-lesscss/

* [flask-peewee](https://github.com/coleifer/flask-peewee)
* User auth
  * https://github.com/mattupstate/flask-social
  * http://pythonhosted.org/Flask-Security/quickstart.html
* Procfile
  * https://github.com/kennethreitz/flask-heroku/
* Celery
  * http://flask.pocoo.org/docs/patterns/celery/
* Sentry (link)

* One file example
* Monolithic app example
* Blueprint example
  https://gist.github.com/coleifer/3bee9ad91aea3b56b11c

## Usage

Have a look at the [example project]()

## Development

Install the development requirements (in a virtualenv, after cloning the repo:

    pip install -r development.txt

Run the tests with:

    nosetests

Run the development server with:

    python -m drain

Run the linting (pep8, pyflakes) with:

    flake8 drain 

## API documentation ##

To generate the documentation:

    cd docs && PYTHONPATH=.. make singlehtml
