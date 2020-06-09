for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    flag=1
    for i in range(n):
        if(l.count(i)==2):
            flag=0
            print(0)
            break
    if flag==0:
        continue
    
    m=abs(l[0]-l[1])
    for i in range(n-1):
    
        #print("--")
        for j in range(i+1,n):
            #print("==")
            if m>abs(l[i]-l[j]):
                #print("-----",m)
                m=abs(l[i]-l[j])
        

    print(m)
    
        
    
                
