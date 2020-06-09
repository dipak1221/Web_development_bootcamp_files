def prime(num):
    for i in range(2,num):
        if(num%i==0):
            return False
    return True

n=int(input())
l=[]
for i in range(1,n+1):
    l.append(i)
m=l.copy()
i=n-1
k=[0]*n

while(i>=0):
    if(k[i]!=0):
        i-=1
        continue
    for j in range(len(m)-1,-1,-1):
        
        if(prime(l[i]+m[j])):
            
            if i==j and i!=0:
                k[i]=m[j]
                k[m.index(m[j])+1]=l[i]
                
            else:
                k[i]=m[j]
                k[m.index(m[j])]=l[i]
           
            m.remove(m[j])

           
            if(len(m)==0):
                break
            m.remove(l[i])


            
            i-=1
            break
    i-=1


    
print(l)
print(k)
    

