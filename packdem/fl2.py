# coding: utf8
import check_function.check_age
def problem1_2():
    print('Общество в начале XXI века')
    age = int(raw_input('enter age: '))
    if check_function.check_age.check(0,7,age):
        print('Вам в детский сад')
    elif check_function.check_age.check(8,18,age):
        print('Вам в школу')
    elif check_function.check_age.check(19,25,age):
        print('Вам в профессиональное учебное заведение')
    elif check_function.check_age.check(26,60,age):
        print('Вам на работу')
    elif check_function.check_age.check(61,120,age):
        print('Вам предоставляется выбор')
    else:
        print('Ошибка! Это программа для людей!\n'*5)

