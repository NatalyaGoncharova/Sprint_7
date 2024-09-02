import pytest
from classes.class_registration import CourierApi
from faker import Faker

fake = Faker()


@pytest.fixture
def create_and_delete_courier():
    login = fake.user_name()
    password = fake.password()
    first_name = fake.first_name()

    response = CourierApi.registrate_courier(login, password, first_name)
    assert response.status_code == 201, f"Failed to create courier: {response.text}"

    login_response = CourierApi.authorize_courier(login, password)
    assert login_response.status_code == 200, f"Failed to login courier: {login_response.text}"

    courier_id = login_response.json().get("id")
    assert courier_id is not None, "Failed to retrieve courier ID"

    yield login, password, courier_id

    delete_response = CourierApi.delete_courier(courier_id)
    assert delete_response.status_code == 200, f"Failed to delete courier: {delete_response.text}"