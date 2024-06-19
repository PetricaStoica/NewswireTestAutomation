import pytest
from pages.newswire_page import NewswirePage

@pytest.fixture
def newswire_page(login):
    return NewswirePage(login)

def test_select_location(newswire_page):
    newswire_page.select_europe_location()
    assert newswire_page.get_selected_location() == 'Europe'
