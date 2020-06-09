l=[]
for i in range(int(input())):
    l.append(int(input()))

print(l)

s=list(set(l))
s.sort(reverse=True)

peeks=[]
ii=0
for i in range(len(l)):
    if s[ii]==l[i]:
        peeks.append(i)
        ii+=1

s.sort()
trough=[]
ii=0
for i in range(len(l)-1,-1,-1):
    if s[ii]==l[i]:
        trough.append(l[i])
        ii+=1


print(max(peeks[-1]-peeks[-2],trough[-1]-trough[-2]))
    
    
    
