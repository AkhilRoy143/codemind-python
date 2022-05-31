num=input()
t=int(num)
r=0
for i in range(len(num)):
    r=r+(int(num[i])**(i+1))
if(r==t):
    print(True)
else:
    print(False)