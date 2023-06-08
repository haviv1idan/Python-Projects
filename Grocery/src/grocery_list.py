# def write_to_csv(table, parsed_data: list[dict[str, str]]):
#     with open(FILENAME, 'a') as f:
#         writer = csv.DictWriter(f, fieldnames=table.headers)
#         writer.writeheader()
#         writer.writerows(parsed_data)
#
# def read_csv(filename):
#     with open(filename, mode='r') as file:
#         reader = csv.DictReader(file)
#         data = [row for row in reader]
#     return data
"""
This script looking for product and get with the website chp.co.il the best prices in selected area
The script work like this:
 - There is JSON of Products
 - Each Product contain all tables content about his price in different shops

Example:
    {
    Product(
        name: milk,
        id: barcode,
        shops:
        {
            index: {
                    content
                }
        },
        online_shops:
        {
        }
    )
}
"""
import json
import logging

from Grocery.src.constants import *
from Grocery.src.classes import *
from selenium import webdriver
from selenium.webdriver.common.by import By


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("grocery_list")


def print_table(table):
    print(("{:<50}" * len(table.headers)).format(*table.headers))
    for row, data in table.body.items():
        print(("{:<50}" * len(table.headers)).format(*data.values()))


def get_products_id_from_file():
    with open("products.txt", 'r') as file:
        products = file.readlines()
    return products


def write_products_to_file(products):
    with open(PRODUCTS_DETAILS, "w") as file:
        file.write(json.dumps(products))


def get_all_products():

    # Clear file
    with open(FILENAME, 'w') as file:
        file.write("")

    browser = webdriver.Firefox()
    browser.get(WEBSITE)
    web_page = WebPage(browser, WEBSITE)
    web_page.fill_product_filter_field(By.NAME, "shopping_address", SHOPPING_AREA)

    products_pool = ProductsPool()
    for product_id in get_products_id_from_file():

        product = Product(product_id)
        tables_list = web_page.get_all_tables()

        for table in tables_list:
            if table.attrs.get("style") == "display: inline-block":
                product.name = table.find("h3").contents[0].text

            # filter non results table
            if "results-table" not in table.attrs.get("class", ""):
                continue

            # Table headers
            headers = [th.text for th in table.find("thead").find("tr").find_all("th")]
            logger.info(f"got headers: {headers}")

            # Table Body
            body_content = [tr for tr in table.find("tbody").find_all("tr")
                            if "display_when_narrow" not in tr.attrs.get("class", "")]
            logger.info(f"got body: {body_content}")

            table_json = {}
            for row_index, tr in enumerate(body_content):
                row_content = {}
                for td_index, td in enumerate(tr.find_all("td")):
                    if headers[td_index] != "מבצע":
                        row_content[headers[td_index]] = td.text
                        continue

                    try:
                        if td.next.get("type") == "button":
                            row_content[headers[td_index]] = td.next["data-discount-desc"]
                    except AttributeError:
                        row_content[headers[td_index]] = td.text

                table_json[row_index] = row_content

            setattr(product, "{}shops".format("online_" if len(headers) == 5 else ""), table_json)

        products_pool.products[product.name] = product.__str__()
        logger.info(f"adding {product.name} to products.\nproduct details:\n{product.__str__()}")

    print(f"products: {json.dumps(products_pool.products)}")

    write_products_to_file(products_pool.products)

    browser.quit()


# try:
#     if os.path.getsize(PRODUCTS_DETAILS) == 0:
#         get_all_products()
# except FileNotFoundError:
#     get_all_products()
