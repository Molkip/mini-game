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

vless://0d3e3326-92ef-4f4e-892c-f3b8881e3d6c@5.129.220.189:443?type=tcp&security=reality&fp=chrome&pbk=l6BgSS_jH0QWHP7Fdm0JUymaBE3RN2kRwi7L-Xln0ws&sni=yandex.ru&sid=118f80&spx=/&flow=xtls-rprx-vision#Чехия-3 🇨🇿