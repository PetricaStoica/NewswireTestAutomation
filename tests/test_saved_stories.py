import pytest
from pages.saved_stories_page import SavedStoriesPage

@pytest.fixture
def saved_stories_page(login):
    return SavedStoriesPage(login)

def test_save_story_success(saved_stories_page):
    saved_stories_page.save_story()
    saved_stories_page.goto('https://newswire.storyful.com/saved')
    assert saved_stories_page.saved_stories_displayed() is True