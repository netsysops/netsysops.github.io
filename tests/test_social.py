"""Tests against the generated json file."""
from helpers import _load_site
from helpers import IGNORED_FILES

HEADER_TEASER_NOT_SET = ""


def test_header_teaser():
    """Test to see that no entries point to the same url."""
    site = _load_site()
    for entry in site:
        content_type = site[entry]['content_type']
        if entry not in IGNORED_FILES and content_type != 'posts':
            if HEADER_TEASER_NOT_SET == site[entry]['header_teaser']:
                assert HEADER_TEASER_NOT_SET == entry
