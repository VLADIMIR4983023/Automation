class Address:
    index = '123456'
    city = 'Город1'
    street = 'Улица1'
    house = 'Дом1'
    apartment = 'Квартира1'

    def __init__(self, index, city, street, house, apartment):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment
