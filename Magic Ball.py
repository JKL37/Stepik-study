import random


def game():
    question = input("Задайте свой вопрос...  ")
    print(question)

    answer = random.choice(answers)
    print(answer)

    another_one()


def another_one():
    print("У вас еще есть вопросы?  ")
    el = input("y - да, n - нет")
    if el == "y":
        game()
    elif el == "n":
        return print("Возвращайся, если возникнут вопросы...")
    else:
        print("Нераспознанная команда, введите заново:")
        another_one()


answers = [
    "Бесспорно",
    "Предрешено",
    "Никаких сомнений",
    "Определенно да",
    "Можешь быть уверен в этом",
    "Мне кажется - да",
    "Вероятнее всего",
    "Хорошие перспективы",
    "Знаки говорят - да",
    "Да",
    "Пока неясно, попробуй снова",
    "Спроси позже",
    "Лучше не рассказывать",
    "Сейчас нельзя предсказать",
    "Сконцетрируйся и спроси опять",
    "Даже не думай",
    "Мой ответ - нет",
    "По моим данным - нет",
    "Перспективы не очень хорошие",
    "Весьма сомнительно",
]

print("Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.")
name = input("Введите Ваше имя: ")
print("Привет,", name)

game()
