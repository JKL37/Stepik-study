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
    count_letter = 0
    rus_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

    while Flag == False:
        letter = input("Введите букву или слово: ").upper()
        if len(letter) == 1:
            if letter in rus_alphabet:
                if letter not in guessed_letters:
                    for i in range(len(word)):
                        if letter == word[i]:
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
                            print("Загаданное слово: ", word)
                            break
                        else:
                            print("Вы не угадали!")
                            guessed_letters.append(letter)

                    guessed = False
                else:
                    print("Вы уже вводили эту букву!")
                    continue
            else:
                print("Нераспознанный символ")
                continue
        else:
            for i in letter:
                if i in rus_alphabet:
                    count_letter += 1
            if count_letter == len(letter):
                if letter == word:
                    print(display_hangman(tries))
                    print(word)
                    print("Вы угадали слово! Вы победили! ")
                    Flag = True
                else:
                    if letter not in guessed_words:
                        tries -= 1
                        print(display_hangman(tries))
                        print(word_completion)
                        if tries == 0:
                            print("Вы проиграли!")
                            print("Загаданное слово: ", word)
                            break
                        else:
                            print("Вы не угадали!")
                            guessed_words.append(letter)
                            count_letter = 0
                    else:
                        print("Вы уже вводили это слово!")
                        continue
            else:
                print("Нераспознанный символ")
                count_letter = 0
                continue


word_list = ["ВИСЕЛИЦА", "УГАДАЙКА", "ПИЛОТ", "ПИТОН", "КОРМ"]


Flag1 = True
while Flag1 == True:
    word = get_word()
    play(word)
    more = input("Вы хотите сыграть еще? ДА или НЕТ  ")
    Flag2 = False
    while Flag2 == False:
        if more == "ДА":
            break
        elif more == "НЕТ":
            Flag1 = False
            print("До свидания!")
            break
        else:
            more = input("Нераспознанная команда, введите заново:  ")
