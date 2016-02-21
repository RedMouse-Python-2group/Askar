def mypow(*args):
    n=False
    tmp=0
    for i in args:
        if n:
            print (pow(i,tmp))
            tmp=i
        else:
            print (i)
            n=True
            tmp=i