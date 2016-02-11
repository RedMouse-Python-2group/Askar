n = int(raw_input("vvedite nomer zadaniy: "))
print(n)
if n==1:
    a = raw_input("enter str:  ")
    a=a.split(' ')
    n=''
    for i in a:
        if len(i)>len(n):
            n=i
    print n
elif n==2:
    a = raw_input("enter str:  ")
    a=a.split(';')
    n=''
    for i in a:
        if len(i)>len(n):
            n=i
    print n
elif n==3:
    print('ne ponyl zadanie')
elif n==4:
    strq=raw_input('vvedite string ')
    if strq.find('dl')==-1:
        print('ne naideno')
    else:
        print('naideno, nahoditsy na ' + str(strq.find('dlf')) + ' pozisii')
elif n==5:
    strq=raw_input('enter string: ')
    print(len(strq.split(' ')))
else:
    print('vvedite ot 1 do 6')