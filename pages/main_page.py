from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class Main_Page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    oil_catalog = "//*[@id='ajax_page']/div[1]/div/div[3]/a/span"


    #Getters
    def get_oil_catalog(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.oil_catalog)))


    #Actions

    def click_oil_catalog(self):
        self.get_oil_catalog().click()

    #Methods

    def catalog_oil(self):
        self.click_oil_catalog()
