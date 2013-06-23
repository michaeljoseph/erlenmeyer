from setuptools import setup
import drain

setup(
    name=drain.__name__,
    version=drain.__version__,
    description=drain.__doc__,
    author='Michael Joseph',
    author_email='michaeljoseph@gmail.com',
    url='http://github.com/michaeljoseph/drain',
    packages=['drain'],
    install_requires=open('requirements.txt').readlines(),
    test_suite='nose.collector',
    extras_require = {
        # mysql
        # postgres
        'heroku':  ['flask-heroku < 0.2.0'],
    }
)
