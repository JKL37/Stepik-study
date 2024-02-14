def eng_coding():
    res = ""
    for i in source_text:
        if i in eng_lower_alphabet:
            cod = ord(i) + key
            if cod > 122:
                cod = cod - 26
            res += chr(cod)
        elif i in eng_upper_alphabet:
            cod = ord(i) + key
            if cod > 90:
                cod = cod - 26
            res += chr(cod)
        else:
            res += i
    return res


def rus_coding():
    res = ""
    for i in source_text:
        if i in rus_lower_alphabet:
            cod = ord(i) + key
            if cod > 1103:
                cod = cod - 32
            res += chr(cod)
        elif i in rus_upper_alphabet:
            cod = ord(i) + key
            if cod > 1071:
                cod = cod - 32
            res += chr(cod)
        else:
            res += i
    return res


def eng_decoding():
    res = ""
    for i in source_text:
        if i in eng_lower_alphabet:
            cod = ord(i) - key
            if cod < 97:
                cod = cod + 26
            res += chr(cod)
        elif i in eng_upper_alphabet:
            cod = ord(i) - key
            if cod < 65:
                cod = cod + 26
            res += chr(cod)
        else:
            res += i
    return res


def rus_decoding():
    res = ""
    for i in source_text:
        if i in rus_lower_alphabet:
            cod = ord(i) - key
            if cod < 1072:
                cod = cod + 32
            res += chr(cod)
        elif i in rus_upper_alphabet:
            cod = ord(i) - key
            if cod < 1040:
                cod = cod + 32
            res += chr(cod)
        else:
            res += i
    return res


direction = int(input("Шифруем(1) или дешифруем(2)?"))
lang = int(input("Алфавит русский(1) или английский(2)?"))
source_text = input("Введите исходный текст: ")
key = int(input("Укажите шаг сдвига: "))

cod = 0

eng_lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
eng_upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

if direction == 1 and lang == 1:
    print(rus_coding())
elif direction == 1 and lang == 2:
    print(eng_coding())
elif direction == 2 and lang == 1:
    print(rus_decoding())
elif direction == 2 and lang == 2:
    print(eng_decoding())
