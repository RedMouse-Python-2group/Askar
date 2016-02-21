# coding: utf8
def problem1_2():
    print('Общество в начале XXI века')
    age = int(raw_input('enter age: '))
    if 0<=age and age<=7:
        print('Вам в детский сад')
    elif 8<=age and age<=18:
        print('Вам в школу')
    elif 19<=age and age<=25:
        print('Вам в профессиональное учебное заведение')
    elif 26<=age and age<=60:
        print('Вам на работу')
    elif 61<=age and age<=120:
        print('Вам предоставляется выбор')
    else:
        print('Ошибка! Это программа для людей!\n'*5)

