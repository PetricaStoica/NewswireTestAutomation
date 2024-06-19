from pages.base_page import BasePage

class NewswirePage(BasePage):
    def select_europe_location(self):
        self.page.click("span:has-text('Location')")
        self.page.click("span:has-text('Europe')")
        self.page.get_by_role("button", name="Apply").click()

    def get_selected_location(self):
        return self.page.locator("#test--pill-location--label").inner_text()
