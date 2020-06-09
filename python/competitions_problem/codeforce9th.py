for i in range(int(input())):
    n=int(input())
    l=n
    i=0
    j=1
    count=0
    li=[]
    #print(len(str()))
    while(i<=len(str(l))):
        m=n%(10*j)
        #print(m,"--",j)
        if(m!=0):
            count+=1
            li.append(m)

        j=j*10
        n=n-m
        i+=1
    print(count)
    for i in li:
        print(i,end=" ")
    print()
    li=[]
    count=0
