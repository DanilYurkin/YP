from random import randint
from data import spisoc

spisoc_el = len(spisoc)  # посчитаем количество элементов в списке spisoc
random_number = randint(0, spisoc_el - 1)

task = list(spisoc.values())[random_number]
word = list(spisoc.keys())[random_number]

print(task)

while True:
    answer = input('Назовите букву или слово: ')

    if len(answer) > 1:
        if answer == word:
            print('вы выграли')
            break
        else:
            print('вы проиграли')
    else:
        c = 0
        for i in range(int(len(word))):
            if answer == word[i]:
                print(f'{i+1} по счету')
                c = c+1
            i = i+1
        print(f'Буква "{answer}"! Количество штук в слове - {c}')
