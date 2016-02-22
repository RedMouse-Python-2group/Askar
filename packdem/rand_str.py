# coding: utf8
import random,re,string
string.lestters =' abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ '
n=''
for i in range(0,30):
    n = n + random.choice(string.letters)
n='qswedksjfskdqwefnskdjf '
b=raw_input('enter string: ')
b='qwe'

result = re.match(b,n)
try:
    print result.group(0)
except:
    pass

