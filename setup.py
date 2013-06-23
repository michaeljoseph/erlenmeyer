from setuptools import setup
import erlenmeyer

setup(
    name=erlenmeyer.__name__,
    version=erlenmeyer.__version__,
    description=erlenmeyer.__doc__,
    author='Michael Joseph',
    author_email='michaeljoseph@gmail.com',
    url='http://github.com/michaeljoseph/erlenmeyer',
    packages=['erlenmeyer'],
    install_requires=open('requirements.txt').readlines(),
    test_suite='nose.collector',
    extras_require = {
        # mysql
        # postgres
        'heroku':  ['flask-heroku < 0.2.0'],
    }
)
