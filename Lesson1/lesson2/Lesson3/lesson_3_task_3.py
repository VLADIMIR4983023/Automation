from Mailing import Mailing
from Address import Address

to_address = Address("123456", "Город1", "Улица1", "Дом1", "Квартира1")
from_address = Address("654321", "Город2", "Улица2", "Дом2", "Квартира2")
cost = 500
track = "ABCD1234"

Mailing = Mailing(to_address, from_address, cost, track)
print(f"Отправление {Mailing.track} из {Mailing.from_address.index}\n"

      f"{Mailing.from_address.city}\n"

      f"{Mailing.from_address.street}\n"

      f"{Mailing.from_address.house} - {Mailing.from_address.apartment} в \n"

      f"{Mailing.to_address.index}\n"

      f"{Mailing.to_address.city}, {Mailing.to_address.street}\n"

      f"{Mailing.to_address.house} - {Mailing.to_address.apartment}\n"

      f"Стоимость {Mailing.cost} рублей.")
