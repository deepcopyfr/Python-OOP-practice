from alphabet import Alphabet, EngAlphabet


def main():

    # Тестирование класса Alphabet.

    lang = 'RU'
    rus_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    rus_alphabet = Alphabet(lang, rus_letters)

    print(f'\n\t--- Тестирование класса Alphabet ---')

    print('\nРусский алфавит:')
    rus_alphabet.display_letters()

    print(f'\n\nКоличество букв в алфавите: \n{rus_alphabet.letters_num()}')

    # Тестирование класса EngAlphabet.

    eng_alphabet = EngAlphabet()

    print(f'\n\t--- Тестирование класса EngAlphabet ---')

    print('\nАнглийский алфавит:')
    eng_alphabet.display_letters()

    print(f'\n\nКоличество букв в алфавите: \n{eng_alphabet.letters_num()}')

    print(f'\nПроверим относится ли буква "f" к английскому алфавиту: ')
    eng_alphabet.is_en_letter('f')

    print(f'\nПроверим относится ли буква "щ" к английскому алфавиту: ')
    eng_alphabet.is_en_letter('щ')

    print(f'\nПример текста на английском языке: {eng_alphabet.example()}')


if __name__ == '__main__':
    main()
