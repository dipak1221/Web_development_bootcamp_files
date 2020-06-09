for i in range(int(input())):
    n,k=map(int,input().split())
    j=2
    i=1
    while(i<=k):
        if n%j==0:
            if(j==2):
                n=n+j*(k-i+1)
                break
            n=n+j
            j=2
            i+=1
            continue
        j=j+1
        
    print(n)
        
