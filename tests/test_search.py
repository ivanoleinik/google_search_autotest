from pages.search import GoogleSearchPage, GoogleShoppingPage
from pages.result import GoogleResultPage


def test_basic_google_search(browser):
    """Ищем сало..."""

    query = 'сало'

    search_page = GoogleSearchPage(browser)
    result_page = GoogleResultPage(browser)

    search_page.load()

    search_page.search(query)

    assert query == result_page.search_input_value()
    assert query in result_page.title()
    for title in result_page.result_link_titles():
        assert query in title.lower()


def test_google_shopping(browser):
    """Ищем, где купить сало..."""
    query = 'сало'

    search_page = GoogleSearchPage(browser)

    search_page.load()

    search_page.search(query)

    shopping_page = GoogleShoppingPage(browser)
    shopping_page.load_goods()

    assert query == shopping_page.search_input_value()
    for title in shopping_page.result_goods_titles()[:10]:
        assert query in title.lower()
    for price in shopping_page.result_goods_prices():
        assert price
    for shop_link in shopping_page.result_goods_shop_links():
        assert shop_link
    for delivery_conditions in shopping_page.result_goods_delivery_conditions():
        assert delivery_conditions


def test_google_shopping_prices(browser):
    """Ищем, где купить дешевое сало..."""
    query = 'сало'

    search_page = GoogleSearchPage(browser)

    search_page.load()

    search_page.search(query)

    shopping_page = GoogleShoppingPage(browser)
    shopping_page.load_goods()

    max_price = shopping_page.filter_prices()
    for price in shopping_page.result_goods_prices():
        assert price <= max_price
