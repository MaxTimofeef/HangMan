import os

clear = lambda: os.system("cls")

input("Привет! отгадай слово по буквам\nнажмите ENTER для продолжения")
clear()
print("Поехали!")

letters = []

word = "автомобиль"

while True:
    letter = input("Введите букву: ")
    letters.append(letter)
    print(letter)
    for symb in word:
        if symb in letters:
            print(symb, end=" ")
        else:
            print("*", end=" ")
    print()