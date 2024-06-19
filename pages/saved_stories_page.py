from pages.base_page import BasePage

class SavedStoriesPage(BasePage):
    def save_story(self):
        self.page.click('svg[aria-hidden="true"][focusable="false"][data-icon="star"]')

    def saved_stories_displayed(self):
        return self.page.locator("div.card-title-container").is_visible()