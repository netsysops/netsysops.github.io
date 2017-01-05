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
    '_pages/cidrblock.md',
    '_pages/jedelman8.md',
    '_pages/itdependsnetworks.md',
    '_pages/mirceaulinic.md'
]


def _load_site():
    with open('_site/site-validation.json') as fs:
        return json.load(fs)
