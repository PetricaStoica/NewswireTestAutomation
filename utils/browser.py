from playwright.sync_api import sync_playwright

class Browser:
    def __init__(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context(viewport={"width": 1920, "height": 1080})
        self.page = self.context.new_page()

    def close(self):
        self.context.close()
        self.browser.close()
        self.playwright.stop()
