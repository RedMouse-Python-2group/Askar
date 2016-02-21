# coding: utf8
def problem1_1():
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
