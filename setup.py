#!/usr/bin/env python

from distutils.core import setup

from djangogenius import __VERSION__

setup(
    name='Django Genius',
    version=__VERSION__,
    description="A Djangoized version of CAYAN's Genius API",
    author='Williams Méndez',
    maintainer='Williams Méndez',
    packages=['djangogenius', 'tests'],
    url='https://github.com/sanaani/django-genius',
    install_requires=[
        'Django>=2.2.2',
        'requests>=2.22',
        'zeep>=3.4.0',
        'django-environ>=0.4.5'
    ],
    classifiers=[
        "Framework :: Django",
        'Framework :: Django :: 2.2',
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
