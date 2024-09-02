from classes.class_order import OrderApi


class TestOrderList:

    def test_get_order_list(self):
        response = OrderApi.get_orders()
        assert response.status_code == 200, f"Expected 200, but got {response.status_code}"
        assert "orders" in response.json(), "No 'orders' in response"
        assert len(response.json()["orders"]) > 0, "Not list"
