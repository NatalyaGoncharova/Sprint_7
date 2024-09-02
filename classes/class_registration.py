import allure
import requests
from urls import *
from helper import CourierData


class CourierApi:
    @staticmethod
    @allure.step("Регистрация курьера в системе")
    def registrate_courier(login, password, first_name):
        url = REGISTRATION_COURIER_URL
        data = CourierData.get_courier_registration_data(login, password, first_name)
        response = requests.post(url, json=data)
        return response

    @staticmethod
    @allure.step("Авторизация курьера в системе")
    def authorize_courier(login, password):
        url = AUTHORIZATION_COURIER_URL
        data = CourierData.get_courier_authorization_data(login, password)
        response = requests.post(url, json=data)
        return response

    @staticmethod
    @allure.step("Удаление курьера в системе")
    def delete_courier(courier_id):
        url = f"{REGISTRATION_COURIER_URL}/{courier_id}"
        response = requests.delete(url)
        return response
