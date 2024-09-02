import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from classes.class_registration import CourierApi
from faker import Faker

fake = Faker()


@pytest.fixture
def create_and_delete_courier():
    login = fake.user_name()
    password = fake.password()
    first_name = fake.first_name()

    CourierApi.registrate_courier(login, password, first_name)
    login_response = CourierApi.authorize_courier(login, password)
    courier_id = login_response.json().get("id")

    yield login, password, courier_id

    CourierApi.delete_courier(courier_id)
