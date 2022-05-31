num=int(input())
sm=0
l=list(map(int,input().split()))
for i in range(len(l)):
    if(l[i]%2==1):
        sm=sm+l[i]
print(sm)
        