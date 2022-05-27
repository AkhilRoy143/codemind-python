num=int(input())
num1=str(num)
r=num**2
r1=str(r)
s=len(str(num))
s1=r1[-s:]
if(num==int(s1)):
    print("Automorphic Number")
else:
     print("Not an Automorphic Number")