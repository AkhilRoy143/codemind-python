def prime(a):
    c=0
    for i in range(1,a+1):
        if a%i==0:
            c+=1
    if c==2:
        return True
    else:
        return False
n=int(input())
x=0
y=0
for i in range(n+1):
    for j in range(i,n+1):
        if prime(i) and i*j==n:
            x=i
            y=j
if x==0 and y==0:
    print(-1)
else:
    print(x,y)