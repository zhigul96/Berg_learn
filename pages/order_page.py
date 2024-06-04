from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class Order_Page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    orders_all = "//span[@class='ico shipment_ico']"

    #Getters
    def get_orders_all(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.orders_all)))

    #Actions

    def click_orders_all(self):
        self.get_orders_all().click()

    #Methods

    def orders(self):
        self.click_orders_all()
