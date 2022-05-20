from typing import Union

from string import ascii_letters
from House import House


class Human:
    """Позволяет создавать множество объектов-людей."""

    __default_name = 'Unknown'
    __default_age = 35

    ### Основные методы ###

    def __init__(self, name: str = __default_name, age: int = __default_age) -> None:
        """Принимает и обрабатывает входные данные."""
        self.__verify_name(name)
        self.__verify_age(age)

        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def display_info(self) -> None:
        """Выводит информацию о человеке."""
        print(f"Имя: {self.name}")
        print(f"Возраст: {self.age} года")
        print(f"Деньги: {self.__money}$")
        print(f"Дом: {self.__house}")

    @staticmethod
    def display_default_info() -> None:
        """Выводит статические поля имени и возраста."""
        print(f"Имя (по умолчанию): {Human.__default_name}")
        print(f"Возраст (по умолчанию): {Human.__default_age}")

    def earn_money(self, money: Union[float, int]) -> None:
        """Пополняет денежные средства."""
        self.__money += money
        print(f"Заработано {money}$! Текущая денежная сумма: {self.__money}$.")

    def __make_deal(self, house: House, price: Union[float, int]) -> None:
        """Тратит денежные средства в ходе сделки и приобретает дом."""
        self.__money -= price
        self.__house = house

    def buy_house(self, house: House, discount: int) -> None:
        """Позволяет приобрести дом, совершая сделку."""
        price = house.final_price(discount)
        self.__verify_money(price)

        self.__make_deal(house, price)
        print(f"Поздравляем! Вы приобрели дом за {price}$.")

    ### Вспомогательный функционал ###

    @staticmethod
    def __verify_name(name: str) -> None:
        """Проверяет корректность ввода имени."""
        if not isinstance(name, str):
            raise TypeError("Имя должно быть строкой")

        if len(name) < 1:
            raise TypeError("Имя должно состоять хотя бы из 1 буквы")

        for letter in name:
            if letter not in ascii_letters:
                raise TypeError(f"Имя должно состоять из букв латинского алфавита")

    @staticmethod
    def __verify_age(age: int) -> None:
        """Проверяет корректность ввода возраста."""
        if not isinstance(age, int):
            raise TypeError("Возраст должен быть целым числом")

        if age < 18 or age > 120:
            raise TypeError("Возраст должен входить в диапазон [18; 120]")

    def __verify_money(self, money: Union[float, int]) -> None:
        """Проверяет корректность ввода суммы сделки."""
        if not isinstance(money, (float, int)):
            raise TypeError("Сумма сделки должна быть вещественным или целым числом")

        if money > self.__money:
            raise ValueError(
                "Сумма сделки не должна превышать количество имеющихся денег")
