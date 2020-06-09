import math

n=list(map(int,input().split()))
m=list(map(int,input().split()))

c=0
for i in n:
    for j in m:
        if math.gcd(i,j)!=1:
            c+=1

print(c)
