import os
import random

clear = lambda: os.system("cls")

input("Привет! отгадай слово по буквам\nнажмите ENTER для продолжения")
clear()
print("Поехали!")

letters = []

words = ['пирожок', 'чебурек', 'огурец', 'сосиска', 'котик', 'квокка', 'корабль', 'самолет', 'автомобиль', 'дирижабль']
word = random.choice(words)

isWin = True
hp = 10

while hp > 0:
    isWin = True
    letter = input("Введите букву: ")
    letters.append(letter)
    print(letter)
    for symb in word:
        if symb in letters:
            print(symb, end=" ")
        else:
            print("*", end=" ")
            isWin = False
    print()

    if isWin:
        print("Ты угадал! Молодец!")
        break

    if letter not in word:
        hp -= 1
        print(f"Осталось попыток: {hp}")

if hp == 0:
    print("Ты проиграл!")