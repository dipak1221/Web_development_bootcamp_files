for i in range(int(input())):
    n,k=map(int,input().split())

    if(n<k):
        print("NO")
    else:
        if n%k==0:
            print("YES")
            for i in range(k):
                print(n//k,end=" ")
            print()
        else:
            q=n//k
            rem=n%k
            if (q+rem)%2!=0 and q%2!=0:
                print("YES")
                for i in range(k-1):
                    print(q,end=" ")
                print(q+rem)
            elif (q+rem)%2==0 and q%2==0:
                print("YES")
                for i in range(k-1):
                    print(q,end=" ")
                print(q+rem)
            else:
                if (k-1)%2!=0:
                    print("NO")
                elif q==1:
                    print("NO")
                else:
                    print("YES")
                    for i in range(k//2):
                        print(q-1,q+1,end=" ")
                    print(q+rem)
                    
                
            
