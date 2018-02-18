from setuptools import setup, find_packages
from tanew.__init__ import __version__ as VERSION

requirements = ['tweepy', 'requests_oauthlib', 'docopt']

setup(
    name='twitter-anew',
    version=VERSION,
    description="hmmm",
    long_description="tbd",
    license='MIT',
    author='Matthew Barber',
    author_email='quitesimplymatt@gmail.com',
    url='https://github.com/Honno/twitter-anew/',
    classifiers=[
        'Programming Language :: Python :: 3'
    ],
    keywords='twitter',
    packages=find_packages(),
    packages_dir={'': 'tanew'},
    install_requirements=requirements,
    entry_points={
        'console_scripts': [
            'tanew=tanew.cli:main'
        ]
    }
)