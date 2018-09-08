import random

letters = 'abcdefghijklmnopqrstuvwxyz'
alphabet = [i for i in letters]
letter = random.choice(alphabet)
index = alphabet.index(letter) + 1
while 1:
    a = input('Введите строчную букву английского алфавита: ')
    if a in alphabet:
        if a == letter:
            print('You are right!', letter)
            break
        elif a != letter:
            index_try = alphabet.index(a_try) + 1
            if index_try < index:
                print('Правильный ответ находится правее :(')
                continue
            else:
                print('Правильный ответ находится левее :(')
                continue
    else:
        print('Но это не буква :((')
        continue


