for i in range(int(input())):
    n,k=map(int,input().split())
    if k>n:
        print("NO")
        continue
    
    if(n%k==0):
        m=n/k
        print("YES")
        l=[int(m)]*k
        for i in l:
            print(i,end=" ")
        print()
        continue
        
    elif n%2==0 and k%2!=0:
        if k>n/2:
            print("NO")
            continue
    
        m=n//k
        if m%2!=0:
            m=m-1
        l=[int(m)]*(k-1)
        l.append(n-sum(l))
        print("YES")
        for i in l:
            print(i,end=" ")
        print()
        continue
    
    elif n%2!=0 and k%2==0:
        print("NO")
        continue
    elif n%2==0 and k%2==0:
        m=n//k
        l=[int(m)]*(k-1)
        l.append(n-sum(l))
        print("YES")
        for i in l:
            print(i,end=" ")
        print()
        continue
        
    elif n%2!=0 and k%2!=0:
        m=n//k
        l=[int(m)]*(k-1)
        l.append(n-sum(l))
        print("YES")
        for i in l:
            print(i,end=" ")
        print()
        continue
        




                    

        
