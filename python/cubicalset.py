for _ in range(int(input())):
    n,m=map(int,input().split())
    
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    
    a=list(set(a))
    b=list(set(b))

    aa=[]
    bb=[]
    
    for i in a:
        for j in b:
            if(((int(round((i*j)**(1./3))))**3)==i*j):
                aa.append(i)
                bb.append(j)
    print(aa,bb)          
    print(len(aa)**2+len(bb)**2)
                
            
