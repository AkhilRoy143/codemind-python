num=int(input())
l=list(map(int,input().split()))
sm=0
for j in range(1,len(l),2):
    sm=sm+l[j]
print(sm)