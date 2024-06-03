class Address:

    def __init__(self, index, city, street, house, apartment):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment

    def index(self):
        print("Индекс:", self._index)

    def city(self):
        print("Город:", self._city)

    def street(self):
        print("Улица:", self._street)

    def house(self):
        print("Дом:", self._house)

    def apartment(self):
        print("Квартира:", self._apartment)
