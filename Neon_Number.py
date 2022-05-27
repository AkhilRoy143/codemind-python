num=int(input())
r=num**2
t=r
x=0
while r:
    d=r%10
    r=r//10
    x=x+d
if(x==num):
    print("Neon Number")
else:
    print("Not Neon Number")