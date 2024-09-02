class CourierData:
    @staticmethod
    def get_courier_registration_data(login, password, first_name):
        return {"login": login,
                "password": password,
                "firstName": first_name}

    @staticmethod
    def get_courier_authorization_data(login, password):
        return {"login": login,
                "password": password}

    @staticmethod
    def get_order_data(first_name, last_name, address, metro_station, phone, rent_time, delivery_date, comment, colors):
        return {"firstName": first_name,
                "lastName": last_name,
                "address": address,
                "metroStation": metro_station,
                "phone": phone,
                "rentTime": rent_time,
                "deliveryDate": delivery_date,
                "comment": comment,
                "color": colors}