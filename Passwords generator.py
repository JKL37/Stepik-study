import random


def generate_password(length, chars):
    password = ""
    for _ in range(length):
        password += random.choice(chars)
    print(password)


digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"

chars = ""
chars_end = ""

count = int(input("Введите количество паролей для генерации: "))
length = int(input("Введите длину одного пароля: "))
inc_digit = input("Включать ли цифры? ")  # да - нет
inc_up_alpha = input("Включать ли прописные буквы? ")
inc_low_alpha = input("Включать ли строчные буквы? ")
inc_sym = input("Включать ли символы? ")
del_sym = input("Исключить ли неоднозначные символы il1Lo0O? ")

if inc_digit == "да":
    chars += digits
if inc_up_alpha == "да":
    chars += uppercase_letters
if inc_low_alpha == "да":
    chars += lowercase_letters
if inc_sym == "да":
    chars += punctuation
if del_sym == "да":
    for i in chars:
        if i not in "il1Lo0O":
            chars_end += i
    chars = chars_end

for _ in range(count):
    generate_password(length, chars)
