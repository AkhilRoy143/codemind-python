num=int(input())
ln=len(str(num))
l=[]
c=0
while num:
    d=num%10
    num=num//10
    l.append(d)
for i in range(len(l)):
    c=c+l.count(l[i])
if(c==ln):
    print("Unique Number")
else:
    print("Not Unique Number")