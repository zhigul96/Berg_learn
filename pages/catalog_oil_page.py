from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class Catalog_Oil_Page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    motor_oil = "//img[@alt='Моторное масло']"


    #Getters
    def get_motor_oil(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.motor_oil)))


    #Actions

    def click_motor_oil(self):
        self.get_motor_oil().click()

    #Methods

    def select_motor_oil(self):
        self.click_motor_oil()
