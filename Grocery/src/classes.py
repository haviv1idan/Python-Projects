import time

import bs4
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By


class Product:
    """
    This class represent product object
    """
    def __init__(self, product_id):
        self.id: str = product_id
        self.name: str = ""
        self.shops: set | None = None
        self.online_shops: set | None = None

    def __str__(self):
        return {"name": self.name, "id": self.id, "shops": self.shops, "online_shops": self.online_shops}


class ProductsPool:

    def __init__(self):
        self.products: dict[str, dict[str, str]] = {}


class WebPage:
    """
    This class represent web page object per product
    """

    def __init__(self, browser, url: str, product: Product = None):
        self.browser = browser
        self.url: str = url
        self.product: Product = product

    def fill_product_filter_field(self, field_type: By.NAME | By.ID, field_name: str, value: str):
        # Fill the searching field
        product_indicator = self.browser.find_element(field_type, field_name)
        product_indicator.send_keys("")
        product_indicator.send_keys(value)

    def get_all_tables(self) -> list[bs4.element.Tag]:
        """
        find all tables in the given browser
        :return: list of all tables in the given page
        """

        # Fill the searching field
        self.fill_product_filter_field(By.NAME, "product_name_or_barcode", self.product.id)

        # Click on the search button
        self.browser.find_element(By.ID, "get_compare_results_button").click()
        time.sleep(1)

        table_html = self.browser.page_source
        soup = BeautifulSoup(table_html, "html.parser")
        result_div = soup.find("div", {"id": "compare_results"})
        tables: list[bs4.element.Tag] = [table for table in result_div.find_all("table")]

        return tables
