# !/usr/bin/env python
import os
import sys

import django
from django.conf import settings
from django.test.runner import DiscoverRunner

import environ

ROOT_DIR = (environ.Path(__file__) - 2)
env = environ.Env()
env.read_env(str(ROOT_DIR.path(".env")))

DEFAULT_SETTINGS = dict(
    INSTALLED_APPS=[
        'djangogenius',
    ],
    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": "test.db"
        }
    },
    GENIUS_MERCHANT_NAME=env.str('GENIUS_MERCHANT_NAME'),
    GENIUS_MERCHANT_SITE_ID=env.str('GENIUS_MERCHANT_SITE_ID'),
    GENIUS_MERCHANT_KEY=env.str('GENIUS_MERCHANT_KEY'),
    GENIUS_WEB_API_KEY=env.str('GENIUS_WEB_API_KEY'),
    GENIUS_MERCHAT_TRANSPORT_SERVICE_WSDL=str(ROOT_DIR.path('djangogenius/wsdl/Credit-test.wsdl'))
)


def runtests(*test_args):
    if not settings.configured:
        settings.configure(**DEFAULT_SETTINGS)

    sys.path.insert(0, str(ROOT_DIR))

    django.setup()

    runner_class = DiscoverRunner
    test_args = ['tests']

    failures = runner_class(verbosity=1, interactive=True, failfast=False).run_tests(test_args)
    sys.exit(failures)


if __name__ == '__main__':
    runtests()
