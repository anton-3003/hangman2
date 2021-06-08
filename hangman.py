import random

MAX_WRONG = 4


# Ф-ция для выбора случайного слова
def get_word():
    WORDS = [
        "skillfactory",
        'testing',
        'blackbox',
        'pytest',
        'unittest',
        'coverage',
    ]
    word = random.choice(WORDS)
    return word.upper()


# Ф-ция для скрытия букв
def get_hide_word(word):
    secret_word = '_' * len(word)
    return secret_word


# Ф-ция проверки буквы в слове
def check_letter(letter, word):
    if letter in word:
        return True
    else:
        return False


# Message about loose
def loose_msg():
    return 'К сожалению, вы проиграли.'


# Message about win
def win_msg():
    return 'Поздравляем, вы выиграли!'


# word = random.choice(WORDS).upper()  # слово, которое нужно будет угадывать
# hide_word = "_" * len(word)  # по одному дефису на каждую букву, которую нужно отгадать

def main():
    wrong = 0  # количество ошибок, которые сделал игрок
    used = []  # буквы, которые игрок уже отгадал
    alpabet = "abcdefghijklmnopqrstuvwxyz"
    word = get_word()
    hide_word = get_hide_word(word)
    print("\t\tДобро пожаловать в игру 'Виселица'!")

    while wrong < MAX_WRONG and hide_word != word:

        print(*hide_word, sep=' ')
        letter = input("\n\nВведите букву: ").upper()
        while letter in used:
            print("Вы уже предлагали букву: ", letter)
            letter = input("\n\nВведите букву: ").upper()
            print(hide_word)
        used.append(letter)
        # проверка наличия буквы в слове
        if letter in word:
            print(f'Да! Буква {letter.upper()} есть в слове!')
            new = ""
            for i in range(len(word)):
                if letter == word[i]:
                    new += letter
                else:
                    new += hide_word[i]
            hide_word = new.upper()
        else:
            print(f'Буквы {letter.upper()} в слове нет.')
            wrong += 1
    # завершение игры
    if wrong == MAX_WRONG:
        print(loose_msg())
    else:
        print(win_msg())
    print("\nБыло загаданно слово", word, ".")
    input("\n\nPress ENTER to EXIT.")


if __name__ == '__main__':
    main()
