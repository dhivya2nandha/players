n=int(input())
for i in range(n):
    l1=[int(i) for i in input().split()]
    l2=[int(i) for i in input().split()]
if(l1==l2):
    print("yes")
else:
    print("no")
