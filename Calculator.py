"""
Give input as:
first line:  x
second line: +,-,×,÷, rem or qtt
third line:  y
"""


x = int(input())
op = input()
y = int(input())
z = x + y
m = x - y
k = x * y
d = x / y
o = x % y
a = x // y

if op == '+':
    print(z)
elif op == '-':
    print(m)
elif op == '×' or op == 'x':
    print(k)
elif op == '÷' or op == '/':
    print(float(d))
elif op == 'rem' or op == 'remainder':
    print(float(o))
elif op == 'quotient' or op == 'qtt':
    print(float(a))
