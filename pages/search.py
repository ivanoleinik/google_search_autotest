from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class GoogleSearchPage:

    URL = 'https://www.google.com/'

    SEARCH_INPUT = (By.NAME, 'q')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def search(self, query):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(query + Keys.RETURN)


class GoogleShoppingPage:

    VISIBLE_TABS = (By.CSS_SELECTOR, '.hdtb-mitem')
    MORE_BUTTON = (By.CSS_SELECTOR, '.rIbAWc')
    HIDDEN_TABS = (By.CSS_SELECTOR, '.znKVS.OSrXXb.tnhqA')
    LINK_TAG = (By.TAG_NAME, 'a')

    SEARCH_INPUT = (By.NAME, 'q')

    RESULT_GOODS_TITLES = (By.CSS_SELECTOR, '.EI11Pd')
    RESULT_GOODS_PRICES = (By.CSS_SELECTOR, '.a8Pemb.OFFNJ')
    RESULT_GOODS_SHOP_LINKS = (By.CSS_SELECTOR, '.aULzUe.IuHnof')
    RESULT_GOODS_DELIVERY_CONDITIONS = (By.CSS_SELECTOR, '.vEjMR')

    PRICE_FILTER = (By.CSS_SELECTOR, '.EQ4p8c.n3Kkaf.HNgvTe')
    PRICE_RANGE = (By.CSS_SELECTOR, '.lg3aE')

    def __init__(self, browser):
        self.browser = browser

    def load_goods(self):
        for tab in self.browser.find_elements(*self.VISIBLE_TABS):
            if 'Покупки' in tab.text:
                tab.find_element(*self.LINK_TAG).click()
                return
        self.browser.find_element(*self.MORE_BUTTON).click()
        for tab in self.browser.find_elements(*self.HIDDEN_TABS):
            if 'Покупки' in tab.text:
                tab.click()
                return

    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        return search_input.get_attribute('value')

    def result_goods_titles(self):
        goods_titles = self.browser.find_elements(*self.RESULT_GOODS_TITLES)
        return [title.text for title in goods_titles if title.text]

    def result_goods_prices(self):
        goods_prices = self.browser.find_elements(*self.RESULT_GOODS_PRICES)
        return [price2float(price.text) for price in goods_prices]

    def result_goods_shop_links(self):
        goods_shop_links = self.browser.find_elements(*self.RESULT_GOODS_SHOP_LINKS)
        return [shop_link.text for shop_link in goods_shop_links]

    def result_goods_delivery_conditions(self):
        goods_delivery_conditions = self.browser.find_elements(*self.RESULT_GOODS_DELIVERY_CONDITIONS)
        return [delivery_conditions.text for delivery_conditions in goods_delivery_conditions]

    def filter_prices(self):
        price_range = self.browser.find_element(*self.PRICE_FILTER)
        max_price = price2float(price_range.find_element(*self.PRICE_RANGE).text)
        price_range.find_element(*self.LINK_TAG).click()
        return max_price


def price2float(price):
    return float(''.join((filter(lambda x: x == ',' or x.isdigit(), price))).replace(',', '.'))
