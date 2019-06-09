s=input()
l=list(s)
n=len(l)
a=[]
for i in range(n):
    if(l[i] not in a):
        a.append(l[i])
st=''.join(a)
print(st)
