n=int(input())
s=0
while(n>0):
    t=n%10
    s=s+(t*t)
    n=n//10
print(s)
    
