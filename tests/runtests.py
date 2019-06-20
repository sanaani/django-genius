# !/usr/bin/env python
import os
import sys

import django
from django.conf import settings
from django.test.runner import DiscoverRunner

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
)


def runtests(*test_args):
    if not settings.configured:
        settings.configure(**DEFAULT_SETTINGS)

    parent = os.path.dirname(os.path.abspath(__file__))
    parent = os.path.join(parent, '../')
    sys.path.insert(0, parent)

    django.setup()

    runner_class = DiscoverRunner
    test_args = ['tests']

    failures = runner_class(
        verbosity=1, interactive=True, failfast=False).run_tests(test_args)
    sys.exit(failures)


if __name__ == '__main__':
    runtests()
