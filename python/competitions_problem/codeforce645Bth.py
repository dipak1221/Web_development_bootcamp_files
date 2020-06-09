n,d=map(int,input().split())
l=list(map(int,input().split()))
k=[]
for i in l:
    k.extend(list(range(1,i+1)))
#print(k)
o=k.index(max(k))

if(o-d>0):
    print(sum(k[o:o-d:-1]))
else:
    sum1=k[0]
    sum1+=sum(k[o:0:-1])
    sum1+=sum(k[len(k)+o-d+1:])
    print(sum1)
    #print(k[0],k[o:0:-1],k[len(k)+o-d+1:])
    
        
