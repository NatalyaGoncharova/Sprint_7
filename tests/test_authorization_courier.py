from classes.class_registration import CourierApi
from faker import Faker
from data import *
import allure

fake = Faker()


class TestRegistrationCourier:
    @allure.title("Авторизация курьера с валидными данными")
    def test_authorization_courier_success(self, create_and_delete_courier):
        login, password, courier_id = create_and_delete_courier

        response = CourierApi.authorize_courier(login, password)

        assert response.status_code == 200, f"Expected 200, but got {response.status_code}"
        assert response.json()["id"] is not None, "Expected 'id' not to be None"

    @allure.title("Авторизация курьера с в пустым логином")
    def test_test_authorization_courier_missing_login(self):
        password = fake.password()
        login = ""
        response = CourierApi.authorize_courier(login, password)
        assert response.status_code == 400, f"Expected 400, but got {response.status_code}"
        assert response.json().get("message") == RESPONSE_LOGIN_MISS_DATA, f"Expected {'message': {RESPONSE_LOGIN_MISS_DATA}}"

    @allure.title("Авторизация курьера с пустым паролем")
    def test_test_authorization_courier_missing_password(self):
        login = fake.user_name()
        password = ""
        response = CourierApi.authorize_courier(login, password)
        assert response.status_code == 400, f"Expected 400, but got {response.status_code}"
        assert response.json().get("message") == RESPONSE_LOGIN_MISS_DATA, f"Expected {'message': {RESPONSE_LOGIN_MISS_DATA}}"

    @allure.title("Авторизация курьера с несуществующими данными")
    def test_test_authorization_courier_nonexistent_data(self):
        login = fake.user_name()
        password = fake.password()
        response = CourierApi.authorize_courier(login, password)
        assert response.status_code == 404, f"Expected 404, but got {response.status_code}"
        assert response.json().get(
            "message") == RESPONSE_LOGIN_NO_DATA, f"Expected {'message': {RESPONSE_LOGIN_NO_DATA}}"
