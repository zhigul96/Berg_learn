from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class Finish_Bid_Page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    bid_number = "//*[@id='content']/div[1]/div[2]/div[2]/h1/a"
    title_finish_bid = "//span[@class='breadcrumbs__link']"

    #Getters
    def get_bid_number(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.bid_number)))

    def get_title_finish_bid(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.title_finish_bid)))

    #Actions

    def click_bid_number(self):
        self.get_bid_number().click()

    def value_bid_number(self):
        value_finish_order = self.get_bid_number().get_attribute("href")
        return value_finish_order



    #Methods

    def finish_bid(self):
        self.assert_word(self.get_title_finish_bid(), "Оформление заказа", "Заказ создаётся")
        value_num = self.value_bid_number()
        self.click_bid_number()
        return value_num
