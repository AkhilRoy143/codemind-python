n=int(input())
sum=0
a=0
b=1
c=0
for i in range(n):
    print(c,end=' ')
    c=a+b
    b=a
    a=c