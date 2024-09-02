import pytest
from classes.class_order import OrderApi
from faker import Faker

fake = Faker()


class TestCreateOrder:

    @pytest.mark.parametrize("colors", [
        (["BLACK"]),
        (["GREY"]),
        (["BLACK", "GREY"]),
        (None)
    ])
    def test_create_order(self, colors):
        order_data = {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "address": fake.address(),
            "metro_station": fake.random_int(min=1, max=100),
            "phone": fake.phone_number(),
            "rent_time": fake.random_int(min=1, max=24),
            "delivery_date": str(fake.date_this_year()),
            "comment": fake.sentence(),
            "colors": colors
        }

        response = OrderApi.create_order(**order_data)

        assert response.status_code == 201, f"Expected 201, but got {response.status_code}"
        assert "track" in response.json(), "Response JSON does not contain 'track'"
        assert response.json()["track"] is not None, "Track ID should not be None"

        print(f"Test passed with colors: {colors}, track ID: {response.json()['track']}")
