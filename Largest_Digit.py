num=int(input())
l=[]
while num:
    d=num%10
    num=num//10
    l.append(d)
print(max(l))