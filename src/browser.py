from playwright.sync_api import sync_playwright
from config import BROWSER_PROFILE


class Browser:

    def __init__(self):
        self.playwright = None
        self.context = None
        self.page = None

    def start(self):

        self.playwright = sync_playwright().start()

        self.context = self.playwright.chromium.launch_persistent_context(
            user_data_dir=str(BROWSER_PROFILE),
            channel="chrome",
            headless=False,
            viewport=None,
            args=[
                "--start-maximized",
            ],
        )

        if self.context.pages:
            self.page = self.context.pages[0]
        else:
            self.page = self.context.new_page()

        return self.page

    def close(self):

        if self.context:
            self.context.close()

        if self.playwright:
            self.playwright.stop()