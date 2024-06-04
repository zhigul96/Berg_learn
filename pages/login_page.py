from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class Login_Page(Base):
    url = "https://pre.portal.webberg.ru/"
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    entry = "//a[@class='user_panel__login blue_popup__link user_panel__auth_link user_panel__login_link']"
    username = "//input[@name='_username']"
    password = "//input[@name='_password']"
    login_click = "//input[@class='button login__submit_button button_blue button_xl']"

    #Getters
    def get_entry(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.entry)))

    def get_username(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.username)))

    def get_password(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_click(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.login_click)))

    #Actions

    def click_entry(self):
        self.get_entry().click()

    def input_username(self, username):
        self.get_username().send_keys(username)

    def input_password(self, password):
        self.get_password().send_keys(password)

    def login_button(self):
        self.get_login_click().click()

    #Methods

    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.click_entry()
        self.input_username("test_CI_MSK")
        self.input_password("SR20Z4sV1ZcB")
        self.login_button()









