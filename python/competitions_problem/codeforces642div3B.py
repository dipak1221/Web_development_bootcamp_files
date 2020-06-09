for i in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a.sort()
    b.sort()

    if(a[0]<b[-1]):
        for i in range(k):
            if(a[i]<b[n-i-1]):
                a[i],b[n-i-1]=b[n-i-1],a[i]
        #print(a)
        print(sum(a))
    else:
        print(sum(a))

        
        
