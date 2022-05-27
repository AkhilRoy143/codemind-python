num=int(input())
s=""
while num:
    d=num%10
    num=num//10
    s=s+str(d)
print(s)
