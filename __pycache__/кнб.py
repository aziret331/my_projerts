import random

options = ['камень', 'ножницы', 'бумага']
computer = random.choice(options)
player = input('камень, ножницы или бумага?')
if player == computer:
    print('Ничья')
    print('Компьютер выбрал', computer)
elif (player == 'камень' and computer == 'ножницы') or \
     (player == 'ножницы' and computer == 'бумага') or \
     (player == 'бумага' and computer == 'камень'):
    print('Вы победили!')
else:
    print('Компьютер победил!')
    print('Компьютер выбрал', computer)

     
