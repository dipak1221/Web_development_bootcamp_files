for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    countlist=[]
    j=0
    while j<len(l):
        count=1
        while j<(len(l)-1):
            if l[j+1]-l[j]<=2:
                count+=1
                j+=1
            else:
                break
        
        countlist.append(count)
        j+=1

    print(min(countlist),max(countlist))
    
