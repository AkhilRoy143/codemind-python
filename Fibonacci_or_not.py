num=int(input())
a=0
b=1
c=1
l=[a,b]
while c<=num:
    c=a+b
    a=b
    b=c
    l.append(c)
print(num in l)    