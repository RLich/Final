import random
import string
import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Application:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(3)

    def open_page(self, url):
        wd = self.wd
        wd.get(url)

    def login(self, username, password):
        wd = self.wd
        username_box = wd.find_element_by_name
        username_box("username").clear()
        username_box("username").send_keys(username)

        password_box = wd.find_element_by_name
        password_box("password").clear()
        password_box("password").send_keys(password)

        wd.find_element_by_name("login").submit()

    def waiter(self):
        wd = self.wd
        wait = WebDriverWait(wd, 10)
        return wait

    def enter_admin_catalog(self):
        wd = self.wd
        wait = self.waiter()
        xpath = "//ul[@id='box-apps-menu']//span[@class='name']"
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpath)))
        box_apps = wd.find_elements_by_xpath(xpath)
        for box_app in box_apps:
            if box_app.text == "Catalog":
                box_app.click()
                break

    def random_string(self, min_len, max_len):
        symbols = string.ascii_letters + string.digits
        return "".join([random.choice(symbols) for i in range(random.randrange(min_len, max_len))])

    def random_number(self, min_len, max_len):
        digits = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
        return "".join([random.choice(digits) for i in range(random.randrange(min_len, max_len))])

    def add_new_product(self, category_name, product_name, price, quantity):
        wd = self.wd

        # Click on "Add New Product" button
        wd.find_element_by_xpath(("//ul[@class='list-inline pull-right']//a[contains(@href, 'edit_product')]")).click()

        # Enable new product
        wd.find_element_by_xpath("//div[@class='btn-group btn-block btn-group-inline']/label[@class='btn btn-default']").click()

        # Set category
        wd.find_element_by_xpath("//div[@class='form-control']//input[@data-name='Root']").click()
        wd.find_element_by_xpath("//div[@class='form-control']//input[@data-name='%s']" % category_name).click()

        # Set product name
        product_name_box = wd.find_element_by_name("name[en]")
        product_name_box.clear()
        product_name_box.send_keys(product_name)

        # Move to Prices tab
        wd.find_element_by_partial_link_text("Prices").click()

        # Set price
        price_box = wd.find_element_by_xpath("//div[@class='input-group']//input[@name='prices[USD]']")
        price_box.clear()
        price_box.send_keys(price)

        # Move to stock
        wd.find_element_by_partial_link_text("Stock").click()

        # Set quantity
        quantity_box = wd.find_element_by_xpath("//table[@id='table-stock']//input[@name='quantity']")
        quantity_box.clear()
        quantity_box.send_keys(quantity)

        # Submit product
        wd.find_element_by_name("save").click()

    def enter_shop_catalog(self):
        wd = self.wd
        wd.find_element_by_xpath("//a[@title='Catalog']").click()

    def enter_selected_category(self, category_name):
        wd = self.wd
        wd.find_element_by_xpath("//aside[@id='sidebar']//a[text()[contains(., '%s')]]" % category_name).click()

    def check_product_name_with(self, product_name):
        wd = self.wd
        product_names = wd.find_elements_by_xpath("//div[@class='products row half-gutter']//div[@class='name']")
        for name in product_names:
            if name.text == product_name:
                return True
        return False

    def get_product_sticker(self, product_name):
        wd = self.wd
        return wd.find_element_by_xpath("//div[@data-name='%s']//div[@title='New']" % product_name).text

    def enter_product(self, product_name):
        wd = self.wd
        wd.find_element_by_xpath("//div[@data-name='%s']//div[@title='New']" % product_name).click()

    def get_product_stock_status(self):
        wd = self.wd
        return wd.find_element_by_xpath("//div[@class='stock-available']//span[@class='value']").text

    def get_number_of_products_in_cart(self):
        wd = self.wd
        return wd.find_element_by_xpath("//div[@id='cart']//span[@class='quantity']").text

    def add_product_to_cart(self):
        wd = self.wd
        wd.find_element_by_xpath("//button[@name='add_cart_product']").submit()

    def close_product_window(self):
        wd = self.wd
        wd.find_element_by_xpath("//div[@aria-label='Close']").click()
        time.sleep(0.75)

    def enter_cart(self):
        wd = self.wd
        wd.find_element_by_id("cart").click()

    def fill_customer_details(self, firstname, lastname, address1, postcode, city, email, phone):
        wd = self.wd

        firstname_box = wd.find_element_by_name("firstname")
        firstname_box.clear()
        firstname_box.send_keys(firstname)

        lastname_box = wd.find_element_by_name("lastname")
        lastname_box.clear()
        lastname_box.send_keys(lastname)

        address1_box = wd.find_element_by_name("address1")
        address1_box.clear()
        address1_box.send_keys(address1)

        postcode_box = wd.find_element_by_name("postcode")
        postcode_box.clear()
        postcode_box.send_keys(postcode)

        city_box = wd.find_element_by_name("city")
        city_box.clear()
        city_box.send_keys(city)

        email_box = wd.find_element_by_name("email")
        email_box.clear()
        email_box.send_keys(email)

        phone_box = wd.find_element_by_name("phone")
        phone_box.clear()
        phone_box.send_keys(phone)

        wd.find_element_by_name("save_customer_details").click()

    def confirm_order(self):
        wd = self.wd
        wait = self.waiter()

        wait.until(expected_conditions.element_to_be_clickable((By.NAME, "confirm_order")))
        wd.find_element_by_name("confirm_order").click()

    def get_error_code(self):
        wd = self.wd
        return wd.find_element_by_xpath("//div[@class='error-code']").text

    def destroy(self):
        self.wd.quit()
