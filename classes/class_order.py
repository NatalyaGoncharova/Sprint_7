import allure
import requests
from urls import *
from helper import CourierData


class OrderApi:
    url = ORDER_URL

    @staticmethod
    @allure.step("Создание заказа")
    def create_order(first_name, last_name, address, metro_station, phone, rent_time, delivery_date, comment,
                     colors=None):
        order_data = CourierData.get_order_data(first_name, last_name, address, metro_station, phone, rent_time, delivery_date, comment, colors)
        response = requests.post(OrderApi.url, json=order_data)
        return response

    @staticmethod
    @allure.step("Получение заказа")
    def get_orders():
        response = requests.get(OrderApi.url)
        return response
