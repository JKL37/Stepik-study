import random


def begin():
    global a, b, c, count
    a = random.randint(1, 100)
    count = 0
    b = guess()
    c = guess_more()


def is_valid(answer):
    if 1 <= int(answer) <= 100:
        return True
    else:
        return False


def guess():

    n = input("Введите число от 1 до 100:")
    while is_valid(n) == False:
        n = input("Некорректное число! Введите заново:")
    return int(n)


def guess_more():
    global a, b, c, count

    while b != a:
        if b > a:
            print("Вы не угадали! Задуманное число меньше")
            count += 1
            b = guess()
        if b < a:
            print("Вы не угадали! Задуманное число больше")
            count += 1
            b = guess()
    else:
        count += 1
        print("Вы угадали c", count, "попытки!")
        print("Хотите сыграть еще? y - да, n - нет")
        ans = input()
        while ans != "y" and ans != "n":
            print("Нераспознанная команда, введите еще раз: ")
            ans = input()
        if ans == "y":
            begin()
        elif ans == "n":
            return print("Спасибо, что поиграли в угадайку. Еще увидимся...")


print("Добро пожаловать в числовую угадайку!")
a = 0
count = 0
b = None
c = None
begin()
