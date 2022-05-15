from selenium.webdriver.common.by import By


class GoogleResultPage:

    SEARCH_INPUT = (By.NAME, 'q')
    RESULT_LINK_TITLES = (By.CSS_SELECTOR, '.LC20lb.MBeuO.DKV0Md')

    def __init__(self, browser):
        self.browser = browser

    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        return search_input.get_attribute('value')

    def title(self):
        return self.browser.title

    def result_link_titles(self):
        link_titles = self.browser.find_elements(*self.RESULT_LINK_TITLES)
        return [title.text for title in link_titles if title.text]
