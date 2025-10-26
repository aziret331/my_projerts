import random
words=['кот ', 'книга', 'шкаф','окно', 'ручка', 'тетрадь', 'телефон', 'компьютер','программа']
word=random.choice(words)
guess = input('угадайте слово: ')
if guess == word:
    print('Вы угадали')
else:
    print('Вы не угадали! загаданное слово было:', word)
