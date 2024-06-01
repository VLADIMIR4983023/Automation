from Mailing import Mailing
from Address import Address

to_address = Address("123456", "Город1", "Улица1", "Дом1", "Квартира1")
from_address = Address("654321", "Город2", "Улица2", "Дом2", "Квартира2")
cost = 500
track = "ABCD1234"

mail = Mailing(to_address, from_address, cost, track)
print(f"Отправление {mail.track} из {mail.from_address.index}\n"

      f"{mail.from_address.city}\n"

      f"{mail.from_address.street}\n"

      f"{mail.from_address.house} - {mail.from_address.apartment} в \n"
      f"{mail.to_address.index}\n"

      f"{mail.to_address.city}, {mail.to_address.street}\n"

      f"{mail.to_address.house} - {mail.to_address.apartment}\n"

      f"Стоимость {mail.cost} рублей.")
