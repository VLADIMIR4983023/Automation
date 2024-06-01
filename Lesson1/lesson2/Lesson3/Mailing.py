class Mailing:
    to_address = "123456", "Город1", "Улица1", "Дом1", "Квартира1"
    from_address = "654321", "Город2", "Улица2", "Дом2", "Квартира2"
    cost = "500"
    track = "ABCD1234"

    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track
