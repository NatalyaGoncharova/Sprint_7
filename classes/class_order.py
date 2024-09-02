import requests
from urls import *
from data import CourierData


class OrderApi:
    url = ORDER_URL

    @staticmethod
    def create_order(first_name, last_name, address, metro_station, phone, rent_time, delivery_date, comment,
                     colors=None):
        order_data = CourierData.get_order_data(first_name, last_name, address, metro_station, phone, rent_time, delivery_date, comment, colors)
        response = requests.post(OrderApi.url, json=order_data)
        return response

    @staticmethod
    def get_orders():
        response = requests.get(OrderApi.url)
        return response
