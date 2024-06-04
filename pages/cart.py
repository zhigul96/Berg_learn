import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime

from base.base_class import Base
from pages.catalog_select_page import value_price_catalog_1_text
from pages.catalog_select_page import value_price_catalog_2_text
from pages.catalog_select_page import Select_Cat_Page

class Cart_Page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    price_product_1 = "//*[@id='basketForm']/div[1]/div/div/table/tbody/tr[1]/td[8]/span"
    price_product_2 = "//*[@id='basketForm']/div[1]/div/div/table/tbody/tr[2]/td[8]/span"
    sum_bid = "//span[@class='sum']"
    radio_samovyvoz = "//label[@for='berg_cart_goods_list_dispatchType_0']"
    radio_cash = "//label[@for='berg_cart_goods_list_paymentType_0']"
    date_bid = "//input[@id='berg_cart_goods_list_dispatchAt']"
    send_order = "//input[@id='send_order']"
    radio_delivery = "//label[@for='berg_cart_goods_list_dispatchType_1']"
    radio_address = "//label[@for='berg_cart_goods_list_addressId_1']"
    radio_card = "//label[@for='berg_cart_goods_list_paymentType_2']"


    #Getters
    def get_price_product_1(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.price_product_1)))

    def get_price_product_2(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.price_product_2)))

    def get_sum_bid(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.sum_bid)))

    def get_radio_samovyvoz(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.radio_samovyvoz)))

    def get_radio_cash(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.radio_cash)))

    def get_date_bid(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.date_bid)))

    def get_send_order(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.send_order)))

    def get_radio_delivery(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.radio_delivery)))

    def get_radio_address(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.radio_address)))

    def get_radio_card(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.radio_card)))

    #Actions

    def click_radio_samovyvoz(self):
        self.get_radio_samovyvoz().click()

    def click_radio_cash(self):
        self.get_radio_cash().click()

    def click_send_order(self):
        self.get_send_order().click()

    def text_date_bid(self):
        date = self.get_date_bid().get_attribute("value")
        return date

    def value_prod_1(self):
        value_product_1 = self.get_price_product_1().text
        value_product_1 = self.str_to_float(value_product_1)
        return value_product_1

    def value_prod_2(self):
        value_product_2 = self.get_price_product_2().text
        value_product_2 = self.str_to_float(value_product_2)
        return value_product_2

    def value_sum_bid(self):
        value_sum_bid = self.get_sum_bid().text
        value_sum_bid = self.str_to_float(value_sum_bid)
        value_sum_bid = float(value_sum_bid)
        return value_sum_bid

    def value_finish_bid(self):
        value_bid = float(self.value_prod_1()) + float(self.value_prod_2())
        return value_bid

    def click_radio_delivery(self):
        self.get_radio_delivery().click()

    def click_radio_address(self):
        self.get_radio_address().click()

    def click_radio_card(self):
        self.get_radio_card().click()



    #Methods

    #Нал/Самовывоз

    def send_bid(self, value_prod_cat_1, value_prod_cat_2):
        self.click_radio_samovyvoz()
        self.value_sum_bid()
        self.click_radio_cash()
        self.text_date_bid()
        self.assert_price_product(value_prod_cat_1, value_prod_cat_2, self.value_prod_1(), self.value_prod_2())
        self.assert_sum_bid(self.value_sum_bid(), self.value_finish_bid())
        self.assert_date_bid(self.text_date_bid())
        self.click_send_order()

    # Нал/Доставка

    def send_bid_delivery(self, value_prod_cat_1, value_prod_cat_2):
        self.click_radio_delivery()
        self.click_radio_address()
        self.value_sum_bid()
        self.click_radio_cash()
        self.text_date_bid()
        self.assert_price_product(value_prod_cat_1, value_prod_cat_2, self.value_prod_1(), self.value_prod_2())
        self.assert_sum_bid(self.value_sum_bid(), self.value_finish_bid())
        self.assert_date_bid(self.text_date_bid())
        self.click_send_order()

    # Карта/Самовывоз
    def send_bid_card(self, value_prod_cat_1, value_prod_cat_2):
        self.click_radio_samovyvoz()
        self.value_sum_bid()
        self.click_radio_card()
        self.text_date_bid()
        self.assert_price_product(value_prod_cat_1, value_prod_cat_2, self.value_prod_1(), self.value_prod_2())
        self.assert_sum_bid(self.value_sum_bid(), self.value_finish_bid())
        self.assert_date_bid(self.text_date_bid())
        self.click_send_order()

