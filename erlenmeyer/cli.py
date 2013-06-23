"""
erlenmeyer
Do a thing from the command line

Usage:
  erlenmeyer [options] <an_identifier>
  erlenmeyer --version

Options:
  -v --verbose                 Show debug output.
  -h --help                    Show this screen.
"""
from docopt import docopt
import requests
# TODO: flask-script
# TODO: flask-docopt

import settings


def an_example_cli(an_identifier):
    response = requests.get(
        settings.EXTERNAL_API_URL,
        params={'ident': an_identifier}
    )
    print(response)

if __name__ == '__main__':
    arguments = docopt(__doc__)
    an_identifier = arguments['<an_identifier>']
    an_example_cli(an_identifier)
