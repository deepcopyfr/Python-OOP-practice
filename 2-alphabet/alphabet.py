from string import ascii_lowercase


class Alphabet:
    """
    Класс используется для работы с алфавитом какого-либо языка.

    Args:
        language(str): Язык.
        letters(str): Буквы алфавита.

    Methods:
        display_letters: Метод выводит буквы алфавита.
        letters_num: Метод подсчитывает количество букв в алфавите.

    """

    ### Основные методы ###

    def __init__(self, language: str, letters: str) -> None:
        self.__verify_language(language)
        self.__verify_letters(letters)

        self.__language = language
        self.__letters = letters

    def display_letters(self) -> None:
        """Выводит буквы алфавита."""
        for letter in self.__letters:
            print(letter, end=' ')

    def letters_num(self) -> int:
        """Считает количество букв в алфавите."""
        counter = 0

        for letter in self.__letters:
            counter += 1

        return counter

    ### Вспомогательные методы ###

    @staticmethod
    def __verify_language(language: str) -> None:
        """Проверяет корректность ввода языка."""
        if not isinstance(language, str):
            raise TypeError("Язык должен быть строкой")

        if len(language) != 2:
            raise ValueError("Запись языка состоит из двух букв")

    @staticmethod
    def __verify_letters(letters: str) -> None:
        """Проверяет корректность ввода букв алфавита."""
        if not isinstance(letters, str):
            raise TypeError("Буквы алфавита должны быть строкой")

        if len(letters) < 12 or len(letters) > 72:
            raise ValueError("Длина алфавита должна входить в диапазон [12; 72]")


class EngAlphabet(Alphabet):
    """
    Класс используется для работы с алфавитом английского языка.

    Methods:
        letters_num: Метод подсчитывает количество букв в алфавите.
        is_en_letter: Метод проверяет вхождение введённой буквы в алфавит.
        example: Метод возвращает пример текста на английском.

    """

    __default_language = 'En'
    __default_letters = ascii_lowercase

    ### Основные методы ###

    def __init__(self):
        super().__init__(EngAlphabet.__default_language,
                         EngAlphabet.__default_letters)

    @staticmethod
    def __letters_num() -> int:
        """Считает количество букв в алфавите."""
        counter = 0

        for letter in EngAlphabet.__default_letters:
            counter += 1

        return counter

    def letters_num(self) -> int:
        """Считает количество букв в алфавите (переопределённый метод)."""
        return self.__letters_num()

    def is_en_letter(self, letter: str) -> None:
        """Проверяет вхождение введённой буквы в алфавит."""
        self.__verify_letter(letter)

        if letter in self.__default_letters:
            print(f"Буква {letter} относится к английскому алфавиту")
        else:
            print(f"Буква {letter} не относится к английскому алфавиту")

    @staticmethod
    def example() -> str:
        """Возвращает пример текста на английском."""
        text = ''

        for s in range(10):
            text += EngAlphabet.__default_letters[s]

        return text

    ### Вспомогательные методы ###

    @staticmethod
    def __verify_letter(letter: str) -> None:
        """Проверяет корректность ввода буквы."""
        if not isinstance(letter, str):
            raise TypeError("Буква должна быть строкой")

        if len(letter) != 1:
            raise ValueError("Буква должна состоять из одного символа")
