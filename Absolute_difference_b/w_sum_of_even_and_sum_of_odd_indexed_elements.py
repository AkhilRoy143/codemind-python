num=int(input())
es=0
os=0
l=list(map(int,input().split()))
for i in range(len(l)):
    if(i%2==0):
        es=es+l[i]
    else:
        os=os+l[i]
big=max(es,os)
small=min(es,os)
print(abs(big-small))
        