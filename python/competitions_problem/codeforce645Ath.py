import math
for i in range(int(input())):
    n,m=map(int,input().split())
    sum=n*(m//2)+math.ceil(n/2)*(m%2)
    print(sum)
