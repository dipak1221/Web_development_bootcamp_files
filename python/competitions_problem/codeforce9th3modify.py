for i in range(int(input())):
    n,k=map(int,input().split())
    x=int(k//(n-1))
    if(k+x)%n==0:
        print(k+x-1)
    else:
        print(k+x)
