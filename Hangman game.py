import random


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
        # голова, торс, обе руки, одна нога
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
        # голова, торс, обе руки
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
        # голова, торс и одна рука
        """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
        # голова и торс
        """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
        # голова
        """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
        # начальное состояние
        """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """,
    ]
    return stages[tries]


def get_word():
    return random.choice(word_list).upper()


def play(word):
    print("Давайте сыграем в виселицу!")
    word_completion = "_" * len(word)
    Flag = False
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток
    print(display_hangman(tries))
    print(word_completion)

    while Flag == False:
        letter = input("Введите букву или слово: ")

        if len(letter) == 1:
            for i in range(len(word)):
                if letter.upper() == word[i]:
                    print("Вы угадали букву!")
                    guessed_letters.append(letter)
                    word_completion = (
                        word_completion[:i] + word[i] + word_completion[i + 1 :]
                    )
                    print(display_hangman(tries))
                    print(word_completion)
                    guessed = True
                    if word_completion == word:
                        print("Вы угадали слово! Вы победили! ")
                        Flag = True
            if guessed == False:
                tries -= 1
                print(display_hangman(tries))
                print(word_completion)
                if tries == 0:
                    print("Вы проиграли!")
                    break
                else:
                    print("Вы не угадали!")
                    guessed_letters.append(letter)

            guessed = False

        else:
            if letter.upper() == word:
                print(display_hangman(tries))
                print(word)
                print("Вы угадали слово! Вы победили! ")
                Flag = True
            else:
                tries -= 1
                print(display_hangman(tries))
                print(word_completion)
                if tries == 0:
                    print("Вы проиграли!")
                    break
                else:
                    print("Вы не угадали!")
                    guessed_words.append(letter)


word_list = ["ВИСЕЛИЦА", "УГАДАЙКА", "ПИЛОТ", "ПИТОН", "КОРМ"]

rus_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


Flag1 = True
while Flag1 == True:
    word = get_word()
    play(word)
    more = input("Вы хотите сыграть еще? ДА или НЕТ")
    if more == "ДА":
        continue
    elif more == "НЕТ":
        Flag1 = False
