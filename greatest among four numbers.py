print('a value')
a=int(input())
print('b value')
b=int(input())
print('c value')
c=int(input())
print('d value')
d=int(input())
if a>b and a>c and a>d:
    print('a is big')
elif b>a and b>c and b>d:
    print('b is big')
elif c>a and c>b and c>d:
    print('c is big')
else:
    print('d is big')