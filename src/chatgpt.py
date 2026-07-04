from config import CHATGPT_URL


class ChatGPT:

    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto(CHATGPT_URL)
        self.page.wait_for_load_state("domcontentloaded")