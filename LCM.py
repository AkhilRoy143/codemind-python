a,b=map(int,input().split())
big=max(a,b)
small=min(a,b)
i=2
a=big
while True:
    if(big%small==0):
        print(big)
        break
    else:
        big=a*i
        i+=1