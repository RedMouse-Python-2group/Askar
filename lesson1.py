# coding: utf8
number = int(raw_input('vvedite nomer zadachi: '))
if number==1:
    a = int(raw_input("enter integer 1:9 :  "))
    if 1<=a and a<=3:
        s = raw_input("enter string: ")
        n = int(raw_input("enter integer: "))
        for i in range(0,n):
            print(s)
    elif 4<=a and a<=6:
        m = int(raw_input("enter pow: "))
        print(a ** m)
    elif 7<=a and a<=9:
        for i in range(0,10):
            print(a+1)
    else:
        print("error")
elif number==2:
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
else:
    print('zadachi s takim nomerom net!!!')