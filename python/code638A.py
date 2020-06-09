for i in range(int(input())):
    coins=int(input())
    l=[]
    for i in range(1,coins+1):
        l.append(2**i)
        
    c=coins//2
    c=c//2
    sum1=l[-1]+sum(l[:c])
    sum2=sum(l[c:-1])
    
    print(abs (sum1-sum2))
    
