from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class Orders_All_Page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    order = "//*[@id='content']/div[1]/div[4]/div[1]/table/tbody/tr[1]/td[1]/a[1]"


    #Getters
    def get_order(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.order)))

    #Actions

    def value_order(self):
        value_order_order_all = self.get_order().get_attribute("href")
        return value_order_order_all

    #Methods
    def get_value_order(self, value_finish):
        self.assert_order_number(value_finish, self.value_order())



