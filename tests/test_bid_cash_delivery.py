import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.cart import Cart_Page
from pages.catalog_oil_page import Catalog_Oil_Page
from pages.catalog_select_page import Select_Cat_Page
from pages.finish_bid_page import Finish_Bid_Page
from pages.login_page import Login_Page
from pages.main_page import Main_Page
from pages.order_page import Order_Page
from pages.orders_all_page import Orders_All_Page


def test_bid_cash_del():
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'normal'
    s = Service('C:\\Users\\NazarovSV\\PycharmProjects\\berg_object\\chromedriver.exe')
    driver = webdriver.Chrome(service=s, options=options)
    # driver.set_page_load_timeout(15)
    # driver.implicitly_wait(10)
    login = Login_Page(driver)
    login.authorization()
    select_oil = Main_Page(driver)
    select_oil.catalog_oil()
    select_motor_oil = Catalog_Oil_Page(driver)
    select_motor_oil.select_motor_oil()
    add_prod = Select_Cat_Page(driver)
    value_1, value_2 = add_prod.add_products()
    send_bid_cash = Cart_Page(driver)
    send_bid_cash.send_bid_delivery(value_1, value_2)
    finish_order = Finish_Bid_Page(driver)
    value_num = finish_order.finish_bid()
    order = Order_Page(driver)
    order.orders()
    order_all = Orders_All_Page(driver)
    order_all.get_value_order(value_num)
    driver.quit()
