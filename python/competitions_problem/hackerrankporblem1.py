n=int(input())

l=input().lower()
l=list(l)
for ii in range(int(input())):
    i,j=map(int,input().split())
    k=max(l[i:j+1])
    c=l[i:j+1].count(k)
    print(c)
    #print(c,l[i:j+1],k)
    
