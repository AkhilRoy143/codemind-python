num=input()
s=""
for i in num:
    if i=="0":
        continue
    s=i+s
ln=len(s)
if(s[-1]=="-"):
    print("-"+s[0:-1])
else:
    print(s)