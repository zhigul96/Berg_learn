import datetime
class Base():
    def __init__(self, driver):
        self.driver = driver

    def assert_price_product(self, price_catalog_1, price_catalog_2, price_cart_1, price_cart_2):
        assert price_catalog_1 == price_cart_1
        print("Цена на первый товар в корзине и в каталоге соответствует")
        assert  price_catalog_2 == price_cart_2
        print("Цена на второй товар в корзине и в каталоге соответствует")

    def assert_sum_bid(self, price_bid, result):
        assert price_bid == result
        print("Сумма заказа в корзине верная")


        """Method convert_price str_to_float"""
    def str_to_float(self, value):
        value = value.replace(" ", "")
        value = value.replace(",", ".")
        return value

    def assert_word(self, word, result, word_print):
        value_word = word.text
        assert value_word == result
        print(word_print)


    def assert_date_bid(self, date_bid):
        now_date = datetime.datetime.utcnow().strftime("%d.%m.%Y")
        assert date_bid == now_date
        print("Желаемая дата доставки сегодняшняя")

    def assert_order_number(self, number_finish_bid, number_orders_all):
        assert number_orders_all == number_finish_bid
        print("Заказ на странице заказов присутствует")


