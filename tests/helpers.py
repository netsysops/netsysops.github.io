"""Testing helper functions."""
import json

IGNORED_FILES = [
    'assets/css/main.scss',
    'feed.xml',
    'feed.xml',
    'feed.xslt.xml',
    '_pages/404.md',
    '_site-validation/site-validation.md',
    '_pages/site-validation.md',
    'articles/index.html',
    '_pages/ggabriele.md',
    '_principals/0023-own-your-config.md',
    '_principals/0031-service-catalog.md',
    '_principals/0032-abstract.md',
    '_principals/0033-expose.md',
    '_principals/0034-testing.md',
    '_principals/0035-have-fun.md'
]


def _load_site():
    with open('_site/site-validation.json') as fs:
        return json.load(fs)
