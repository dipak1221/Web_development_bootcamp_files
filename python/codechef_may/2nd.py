from collections import Counter

for i in range(int(input())):
    n,q=map(int,input().split())
    s=input()

    for i in range(q):
        cc=int(input())
        c=Counter(s)
        j=0
        if cc==1:
            print(n-len(c))
            continue
        
        for ii in c:
            c[ii]-=cc
            if c[ii]>=1:
                j+=c[ii]
        print(j)
