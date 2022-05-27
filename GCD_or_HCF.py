a,b=map(int,input().split())
l=[]
big=max(a,b)
small=min(a,b)
for i in range (1,big+1):
    if(a%i==0 and b%i==0):
        l.append(i)
print(max(l))