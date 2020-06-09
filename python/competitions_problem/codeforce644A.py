for i in range(int(input())):
    m,n=map(int,input().split())
    if m==n:
        print(2*m*2*m)
        continue
    if m<=n:
        if 2*m<n:
            print(n*n)
        else:
            print(4*m*m)
    else:
        if 2*n>m:
            print(2*2*n*n)
        else:
            print(m*m)
