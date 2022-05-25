from tomato import Tomato

from random import randint


class TomatoBush:
    """
    Класс 'TomatoBush' предназначен для создания кустов из помидоров и работы с ними.

    Attributes:
        number_of_tomatoes(int): Количество помидоров.

    Methods:
        grow_all: Переводит все томаты на следующий этап созревания.
        all_are_ripe: Проверяет все ли томаты являются спелыми.
        give_away_all: Чистит список томатов после урожая.

    """

    ### Основные методы ###

    MIN_INDEX = Tomato.MIN_INDEX + 20
    MAX_INDEX = Tomato.MAX_INDEX - 130

    def __init__(self, number_of_tomatoes: int) -> None:
        self.__verify_number_of_tomatoes(number_of_tomatoes)

        self.__tomatoes = [Tomato(randint(TomatoBush.MIN_INDEX, TomatoBush.MAX_INDEX))
                           for k in range(number_of_tomatoes)]

    def grow_all(self) -> None:
        """Переводит все томаты на следующий этап созревания."""
        for tomato in self.__tomatoes:
            tomato.grow()

    def all_are_ripe(self) -> bool:
        """Проверяет все ли томаты являются спелыми."""
        for tomato in self.__tomatoes:
            if not tomato.is_ripe():
                return False
        return True

    def give_away_all(self) -> None:
        """Чистит список томатов после урожая."""
        self.__tomatoes = []

    ### Вспомогательные методы ###

    def display_info(self) -> None:
        """Выводит информация о всех помидорах."""
        for tomato in self.__tomatoes:
            tomato.display_info()

    @staticmethod
    def __verify_number_of_tomatoes(number_of_tomatoes: int) -> None:
        """Проверяет корректность ввода количества помидоров."""
        if not isinstance(number_of_tomatoes, int):
            raise TypeError("Количество помидоров должно быть целым числом")

        if number_of_tomatoes < 1:
            raise ValueError("Количество помидоров должно быть больше либо равно 1")
