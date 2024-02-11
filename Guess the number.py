import random

def is_valid(answer):
    if 1 <= int(answer) <= 100:
        return True
    else:
        return False

def guess():
    
    n = input('Введите число от 1 до 100:')
    while is_valid(n) == False:
        n = input('Некорректное число! Введите заново:')
    return int(n)






a = random.randint(1, 100)

print('Добро пожаловать в числовую угадайку!')

b = guess()

while b != a:
    if b > a:
        print('Вы не угадали! Задуманное число меньше')
        b = guess()
    if b < a:
        print('Вы не угадали! Задуманное число больше')
        b = guess()
else:
    print('Вы угадали!')
    print('Спасибо, что поиграли в угадайку. Еще увидимся...')