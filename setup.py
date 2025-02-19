import os

from setuptools import setup, find_packages

VERSION = '0.1.2-dev'

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-keycloak',
    version=VERSION,
    long_description=README,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    extras_require={
        'aio': [
            'aiohttp>=3.4.4,<4; python_full_version>="3.5.3"'
        ],
        'dev': [
            'bumpversion==0.5.3',
            'twine',
        ],
        'doc': [
            'Sphinx==1.4.4',
            'sphinx-autobuild==0.6.0',
        ]
    },
    setup_requires=[
        'pytest-runner',
    ],
    install_requires=[
        'requests',
        'python-jose',
        'Django>=1.11',
    ],
    tests_require=[
        'pytest-django',
        'pytest-cov',
        'mock>=2.0',
        'factory-boy',
        'freezegun'
    ],
    url='https://github.com/Peter-Slump/django-keycloak',
    license='MIT',
    author='Peter Slump',
    author_email='peter@yarf.nl',
    description='Install Django Keycloak.',
    classifiers=[]

)
