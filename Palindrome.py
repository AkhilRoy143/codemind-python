num=int(input())
t=num
s=""
while num:
    d=num%10
    num=num//10
    s=s+str(d)
r=int(s)
if(r==t):
    print(True)
else:
    print(False)