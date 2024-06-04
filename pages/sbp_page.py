from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class SBP_Page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    title_sbp = "//h2[@class='sbp-code']"
    order_number = "//*[@id='app-payment']/div/div[1]/div/div[1]/div[2]/b"
    price_order = "//*[@id='app-payment']/div/div[1]/div/div[3]/div[2]"
    button_card = "//a[@class='button button_blue button_xl link acquiring-button']"
    orders_all = "//span[@class='ico shipment_ico']"

    #Getters
    def get_title_sbp(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.title_sbp)))

    def get_order_number(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.order_number)))

    def get_price_order(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.price_order)))

    def get_button_card(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_card)))

    def get_orders_all(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.orders_all)))

    #Actions

    def click_orders_all(self):
        self.get_orders_all().click()


    #Methods

    def orders(self):
        self.assert_word(self.get_title_sbp(), "Оплата через СБП", "Заказ создается. Осуществляется переход на страницу СБП")
        self.assert_word(self.get_button_card(),"Оплатить банковской картой", "Кнопка 'Оплатить банковской картой' присутствует")
        self.click_orders_all()

