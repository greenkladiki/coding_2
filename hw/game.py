import random
import re

def open_files():

#открытие файлов со списками слов 
    with open('drugs.txt', encoding='utf-8') as file1:
        f1 = file1.read()
        drugs = f1.split('\n')
    with open('sleeps.txt', encoding='utf-8') as file2:
        f2 = file2.read()
        sleeps = f2.split('\n')
    with open('mylist.txt', encoding='utf-8') as file3:
        f3 = file3.read()
        mylist = f3.split('\n')
        
#открытие файлов с мертвыми человечками
    with open('vis1.txt', encoding='utf-8') as file4:
        vis1 = file4.read()
    with open('vis2.txt', encoding='utf-8') as file5:
        vis2 = file5.read()
    with open('vis3.txt', encoding='utf-8') as file6:
        vis3 = file6.read()

    return drugs, sleeps, mylist, vis1, vis2,vis3

def choose_your_fighter(drugs, sleeps, mylist):
    print('Определимся с топиком на сегодня: медицина, сон или еда?')
    a = input('Введите одну из указанных тем: ')

    if a == 'медицина':
        word = random.choice(drugs)
    if a == 'сон':
        word = random.choice(sleeps)
    if a == 'еда':
        word = random.choice(mylist)

    for letter in list(word):
        play_word = re.sub(r'\w', '_ ', word)

    return word, play_word

def starting_now(word, play_word, vis1, vis2, vis3):
    print('Поиграем в угадайку на удачу. У вас в запасе 3 шанса налажать :)')
    print(play_word)

    rightletters = ''
    
    while True:
        guess1 = input('Введите букву русского алфавита:') 
        if len(guess1) != 1:
            print('Попробуйте ввести ОДНУ букву')
            continue
        elif guess1 not in 'йцукенгшщзхъфывапролджэячсмитьбю':
            print('Попробуйте пользоваться кириллицей')
            continue
             
        if guess1 in list(word):
            rightletters += guess1
            pattern = '[^' + rightletters + ']'
            opening_word = re.sub(pattern, '_', word)
            print(opening_word)
        else:
            print(vis1)
            print('Всего 2 шанса промахнуться :(')
            break

    while True:
        guess2 = input('Введите букву русского алфавита:') 
        if len(guess2) != 1:
            print('Попробуйте ввести ОДНУ букву')
            continue
        elif guess2 not in 'йцукенгшщзхъфывапролджэячсмитьбю':
            print('Попробуйте пользоваться кириллицей')
            continue
             
        if guess2 in list(word):
            rightletters += guess2
            pattern = '[^' + rightletters + ']'
            opening_word = re.sub(pattern, '_', word)
            print(opening_word)
        else:
            print(vis2)
            print('Всего 1 шанс промахнуться :((')
            break
        
    while True:
        guess3 = input('Введите букву русского алфавита:') 
        if len(guess3) != 1:
            print('Попробуйте ввести ОДНУ букву')
            continue
        elif guess3 not in 'йцукенгшщзхъфывапролджэячсмитьбю':
            print('Попробуйте пользоваться кириллицей')
            continue
             
        if guess3 in list(word):
            rightletters += guess3
            pattern = '[^' + rightletters + ']'
            opening_word = re.sub(pattern, '_', word)
            print(opening_word)
        else:
            print(vis3)
            print('Ценок!')
            break

    return opening_word, vis1, vis2, vis3
    
def main():
    drugs, sleeps, mylist, vis1, vis2, vis3 = open_files()
    word, play_word = choose_your_fighter(drugs, sleeps, mylist)
    opening_word, vis1, vis2, vis3 = starting_now(word, play_word, vis1, vis2, vis3)
    
if __name__ == '__main__':
    main()
