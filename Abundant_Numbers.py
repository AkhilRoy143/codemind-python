num=int(input())
sm=0
for i in range(1,num):
    if(num%i==0):
        sm=sm+i
if(sm>num):
    print(True)
else:
    print(False)