import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
value_price_catalog_1_text = None
value_price_catalog_2_text = None
class Select_Cat_Page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators
    product_IDEMITSU_1 = "//button[@data-offer-id='202580465-27820-0-0-0']"
    product_IDEMITSU_2 = "//button[@data-offer-id='222700983-27820-0-0-0']"
    cart = "//a[@class='cart_big_ico__link']"
    price_catalog_1 = "//*[@id='ajax_page']/div[3]/div[1]/div[3]/div[1]/div[2]/div/div[1]/table/tbody/tr[1]/td[5]"
    price_catalog_2 = "//*[@id='ajax_page']/div[3]/div[1]/div[3]/div[2]/div[2]/div/div[1]/table/tbody/tr[1]/td[5]"


    #Getters
    def get_product_IDEMITSU_1(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_IDEMITSU_1)))
    def get_product_IDEMITSU_2(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_IDEMITSU_2)))
    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_price_catalog_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_catalog_1)))

    def get_price_catalog_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_catalog_2)))



    #Actions

    def click_product_IDEMITSU_1(self):
        self.get_product_IDEMITSU_1().click()
    def click_product_IDEMITSU_2(self):
        self.get_product_IDEMITSU_2().click()
    def click_cart(self):
        self.get_cart().click()

    def value_price_cat_1(self):
        value_price_catalog_1 = self.get_price_catalog_1()
        global value_price_catalog_1_text
        value_price_catalog_1_text = value_price_catalog_1.text
        value_price_catalog_1_text = self.str_to_float(value_price_catalog_1_text)
        return value_price_catalog_1_text

    def value_price_cat_2(self):
        value_price_catalog_2 = self.get_price_catalog_2()
        global value_price_catalog_2_text
        value_price_catalog_2_text = value_price_catalog_2.text
        value_price_catalog_2_text = self.str_to_float(value_price_catalog_2_text)
        return value_price_catalog_2_text



    #Methods

    def add_products(self):
        self.click_product_IDEMITSU_1()
        self.click_product_IDEMITSU_2()
        value_1 = self.value_price_cat_1()
        value_2 = self.value_price_cat_2()
        self.click_cart()
        return [value_1, value_2]