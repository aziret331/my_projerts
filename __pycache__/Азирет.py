print('Викторина по математике!')
score = 0
answer1 = int(input('Сколько будет 5 + 7? '))
if answer1 == 12:
    print('Правильно!')
    score += 1
if answer1 != 12:
    print('Неправильно. Правильный ответ: 12')
answer2 = int(input('Сколько будет 9 * 3? '))
if answer2 == 27:
    print('Правильно!')
score += 1
if answer2 != 27:
    print('Неправильно:( Правильный ответ: 27')
answer3 = int(input('Сколько будет 15 - 4? '))
if answer3 == 11:
    print('Правильно!')
    score += 1
if answer3 != 11:
    print('Неправильно. Правильный ответ: 11')
answer4 = int(input('Сколько будет 14 / 2? ')) 
if answer4 == 7:
    print('Правильно!')
    score += 1
    if answer4 != 7:
        print('Неправильно. Правильный ответ: 7')
answer5 = int(input('Сколько будет 7 * 6? ')) 
if answer5 == 42:
    print('Правильно!')
    score += 1
if answer5 != 42:
    print('Неправильно. Правильный ответ: 42')
answer6 = int(input('Сколько будет 8 + 5 * 2? '))
if answer6 == 18:
    print('Правильно!')
    score += 1
if answer6 != 18:
    print('Неправильно. Правильный ответ: 18')
answer7 = int(input('Сколько будет 20 - 3? '))
if answer7 == 17:
    print('Правильно!')
    score += 1
if answer7 != 17:
    print('Неправильно. Правильный ответ: 17')
answer8 = int(input('Сколько будет 7 * 7? '))
if answer8 == 42:
    print('Правильно!')
    score += 1
if answer8 != 42:
    print('Неправильно. Правильный ответ: 42')
answer9 = int(input('Сколько будет 18 - 3? '))
if answer9 == 15:
    print('Правильно!')
    score += 1
if answer9 != 15:
    print('Неправильно. Правильный ответ: 15')
answer10 = int(input('Сколько будет 10 + 4? '))
if answer10 == 14:
    print('Правильно!')
    score += 1
if answer10 != 14:
    print('Неправильно. Правильный ответ: 14')
print('Ваш результат:', score, 'из 10')