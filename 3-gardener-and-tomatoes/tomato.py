class Tomato:
    """
    Класс 'Tomato' предназначен для создания помидоров и работы с ними.

    Attributes:
        index(int): Гликемический индекс.

    Methods:
        grow: Переводит томат на следующую стадию созревания.
        is_ripe: Проверяет созрел ли томат.

    """

    __states = {
        0: 'Отсутствует',
        1: 'Цветение',
        2: 'Зеленый',
        3: 'Красный'
    }

    MIN_INDEX = 1
    MAX_INDEX = 200

    ### Основные методы ###

    def __init__(self, index: int) -> None:
        self.__verify_index(index)

        self._index = index
        self._state = min(Tomato.__states)

    def grow(self) -> None:
        """Переводит томат на следующую стадию созревания."""
        self.__verify_state()

        self._state += 1

    def is_ripe(self) -> bool:
        """Проверяет созрел ли томат."""
        if self._state == max(Tomato.__states):
            return True
        return False

    ### Вспомогательные методы ###

    def display_info(self) -> None:
        """Выводит информацию о помидоре."""
        print(f"\t--- Помидор {self} ---")
        print(f"Индекс помидора: {self._index}")
        print(f"Стадия зрелости помидора: {Tomato.__states[self._state]}")
        if self.is_ripe():
            print(f"Помидор созрел\n")
        else:
            print(f"Помидор не созрел\n")

    @staticmethod
    def __verify_index(index: int) -> None:
        """Проверяет корректность ввода индекса."""
        if not isinstance(index, int):
            raise TypeError("Индекс помидора должен быть целым числом")

        if index < Tomato.MIN_INDEX or index > Tomato.MAX_INDEX:
            raise ValueError(f"Индекс помидора должен находиться в диапазоне "
                             f"[{Tomato.MIN_INDEX}; {Tomato.MAX_INDEX}]")

    def __verify_state(self) -> None:
        """Проверяет не выходит ли стадия зрелости за максимальную отметку."""
        if self._state == max(Tomato.__states):
            raise ValueError("Нельзя увеличить стадию помидора, если он созрел")
