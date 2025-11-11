import random

print("Добро пожаловать в игру: Угадай число!")
secret = random.randint(1, 10)

while True:
    guess = input("Введите число от 1 до 10: ")

    if not guess.isdigit():
        print("Введите число!")
        continue

    guess = int(guess)

    if guess == secret:
        print("🎉 Вы угадали!")
        break
    else:
        print("Нет! Попробуйте снова.")

