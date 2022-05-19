from typing import Union


class House:
    """Позволяет создавать множество объектов-домов."""

    ### Основной функционал ###

    def __init__(self, area: int, price: Union[float, int]) -> None:
        self.__verify_area(area)
        self.__verify_price(price)

        self._area = area
        self._price = price

    def final_price(self, discount: int) -> float:
        """Рассчитывает цену с учётом скидки."""
        self.__verify_discount(discount)
        return self._price - (self._price * discount) / 100

    ### Вспомогательный функционал ###

    @staticmethod
    def __verify_area(area: int) -> None:
        """Проверяет корректность ввода площади."""
        if not isinstance(area, int):
            raise TypeError("Площадь должна быть целым числом")

        if area < 1:
            raise ValueError("Площадь не может быть меньше либо равна 0")

    @staticmethod
    def __verify_price(price: Union[float, int]) -> None:
        """Проверяет корректность ввода цены."""
        if not isinstance(price, (float, int)):
            raise TypeError("Цена дома должна быть вещественным или целым числом")

        if price < 0:
            raise ValueError("Цена дома не может быть меньше 0")

    @staticmethod
    def __verify_discount(discount: int) -> None:
        """Проверяет корректность ввода скидки."""
        if not isinstance(discount, int):
            raise TypeError("Скидка должна быть целым числом")

        if discount < 0 or discount > 100:
            raise ValueError("Скидка должна входить диапазон [0; 100]")


class SmallHouse(House):
    __default_area = 40

    def __init__(self, price: Union[float, int]) -> None:
        super().__init__(SmallHouse.__default_area, price)
