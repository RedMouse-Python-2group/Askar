# coding: utf8
import check_function.check_age
def problem1_1():
    a = int(raw_input("enter integer 1:9 :  "))
    if check_function.check_age.check(1,3,a):
        s = raw_input("enter string: ")
        n = int(raw_input("enter integer: "))
        for i in range(0,n):
            print(s)
    elif check_function.check_age.check(4,6,a):
        m = int(raw_input("enter pow: "))
        print(a ** m)
    elif check_function.check_age.check(7,9,a):
        for i in range(0,10):
            print(a+1)
    else:
        print("error")
