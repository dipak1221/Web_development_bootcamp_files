for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    k=[]
    for i in range(n):
        m=[l[i]]
        ii=l[i]
        for j in range(i+1,n):
            for jj in range(j+1,n):
                if(l[jj]%ii==0):
                    ii=l[jj]
                    m.append(l[jj])
        k.append(m)
    print(k)
