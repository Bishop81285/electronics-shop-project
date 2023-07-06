import csv
import json

from settings import CSV_FILE_PATH


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    __csv_path = CSV_FILE_PATH

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) <= 10:
            self.__name = new_name
        else:
            raise Exception('Длина наименования товара превышает 10 символов.')

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        """
        Класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv
        """
        with open(cls.__csv_path) as csvfile:
            reader = csv.DictReader(csvfile)

            row: dict
            for row in reader:
                cls(**row)

    @staticmethod
    def string_to_number(string_numb):
        """
        Статический метод, возвращающий число из числа-строки
        """
        if '.' in string_numb:
            return int(float(string_numb))

        return int(string_numb)

    def __del__(self):
        """
        Деструктор класса Item. Вызывается перед уничтожением объекта.
        """
        Item.all.remove(self)
