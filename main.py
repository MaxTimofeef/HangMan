import os

clear = lambda: os.system("cls")

input("Привет! отгадай слово по буквам\nнажмите ENTER для продолжения")

clear()

word = "автомобиль"

for symd in word:
    print(symd, end=" ")