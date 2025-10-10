from random import randint

number = randint(1,100)
print("Угадай число!")
while True:
    guess = int(input("Введите число: "))
    if guess < number:
        print("Ваше число меньше загаданного")
    if guess > number:
        print("Ваше число больше загаданного")
    if guess == number:
        break
print("Поздравляю, вы отгадали число!")