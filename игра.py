import random

number = random.randint(1, 20)
user = 0
while user != number:
    user = int(input('Введите число от 1 до 20: '))
    if user < number:
        print('Вашe число больше загаданного')
    elif user > number:
        print('Вашe число меньше загаданного')
    else:
        print('Вы угадали число')
 
#  Дз дописать Викторину по математике






