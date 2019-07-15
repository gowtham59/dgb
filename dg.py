z1=int(input())
count=0
inp=[]
m2=['a','a','b','i','k','l']
for i in range (0,z1):
    inp.append(input())
for i in inp:
    s=sorted(i)
    if(m2==s):
        count=count+1
print(count)
