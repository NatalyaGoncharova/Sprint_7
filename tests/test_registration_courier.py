from classes.class_registration import CourierApi
from faker import Faker

fake = Faker()


class TestRegistrationCourier:
    def test_registration_courier_success(self, create_and_delete_courier):
        courier_id = create_and_delete_courier
        login = fake.user_name()
        password = fake.password()
        first_name = fake.first_name()
        response = CourierApi.registrate_courier(login, password, first_name)

        assert response.status_code == 201, f"Expected 201, but got {response.status_code}"
        assert response.json()["ok"] == True, "Expected {'ok': true}"

    def test_registration_duplicate_courier(self):
        login = fake.user_name()
        password = fake.password()
        first_name = fake.first_name()

        response1 = CourierApi.registrate_courier(login, password, first_name)
        assert response1.status_code == 201

        response2 = CourierApi.registrate_courier(login, password, first_name)
        assert response2.status_code == 409, f"Expected 409, but got {response2.status_code}"

    def test_registration_courier_missing_field(self):
        login = fake.user_name()
        password = fake.password()
        first_name = fake.first_name()

        response = CourierApi.registrate_courier(None, password, first_name)
        assert response.status_code == 400, f"Expected 400, but got {response.status_code}"



