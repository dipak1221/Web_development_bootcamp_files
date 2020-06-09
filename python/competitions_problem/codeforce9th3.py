for i in range(int(input())):
    n,k=map(int,input().split())
    i=1
    j=1
    while(i<=k):
        if(j%n!=0):
            if i==k:
                break
            i+=1
            
        j+=1
    print(j)
        
