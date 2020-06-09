
for i in range(int(input())):
    n,m=map(int,input().split())
    l=list(map(int,input().split()))

    sum1=sum(l[:m])
    count=0
    flag=1
    m1=0
    for i in range(len(l)-m+1):
        if sum1==sum(l[i:m+i]):
            count+=1
            if(m+i==len(l)):
                #print(l)
                m1+=1
                flag=0
                break

    if(flag==0 and count==(len(l)-m+1) and count>1 and m1==1):
        ss=''
        for i in l:
            ss+=str(i)+' '
        print(len(l))
        print(ss[:-1])
        continue
    
    mm=[]
    s=[]
    for i in l:
        if i not in s:
            s.append(i)
            
    ll=len(s)
    if ll>m:
        print(-1)
        continue
    
    for i in range(1,ll+1):
        if i not in s:
            mm.extend(s)
            mm.append(i)
            break
    k=[]
    if len(mm)==0:
        k=s
        mm=s

    for i in range(len(l)):
        k.extend(mm)
    #print(k)
    i=0
    j=0
    while i<len(l):
        while j<len(k):
            if l[i]==k[j]:
                i+=1
                j+=1
                break
            j+=1
    print(len(k[:j]))
    ss=''
    for i in k[:j]:
        ss+=str(i)+' '
    print(ss[:-1])
    
    
        
            
            
    


    
