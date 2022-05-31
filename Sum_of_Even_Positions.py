num=int(input())
sm=0
l=list(map(int,input().split()))
for i in range(len(l)):
    if(i%2==0):
        sm=sm+l[i]
print(sm)