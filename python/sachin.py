def gcd(x,y):
    rem=x%y
    if rem==0:
        return y
    else:
        return gcd(y,rem)

for i in range(int(input())):
    n=int(input())
    l=[1]
    k=2
    while(k<=n//2):
        if n%k==0:
            l.append(k)
        k+=1

    l.append(n)

    count=len(l)-1
    for i in range(1,len(l)-1):
        for j in range(i+1,len(l)-1):
            if(gcd(l[i],l[j])==1):
                count+=1
        
    print(l)
    print(count)
