from itertools import combinations
l=[]
n,m=map(int,input().split())
for i in range(1,n+1):
    l.append((i**i)%m)


#print(l)
c=l.count(0)
for i in range(c):
    l.remove(0)
cc=0
for i in range(2,len(l)+1):
    k=list(combinations(l,i))
    print(k)
    #print("------------")
    for i in k:
        if sum(i)%m==0:
            #print(i)
            #print("--------")
            cc+=1

print(cc*(2**c)+c)
print(cc,c)

    
