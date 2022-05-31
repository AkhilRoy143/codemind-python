num=int(input())
l=list(map(int,input().split()))
avg=sum(l)//num
print(avg in l)