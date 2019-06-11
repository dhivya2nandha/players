s=input()
n=int(input())
a=s[::-1]
v=['a','e','i','o','u']
r=[]
for i in range(n):
    if(a[i] not in v):
        r.append(a[i])
t=''.join(r)
print(t)
