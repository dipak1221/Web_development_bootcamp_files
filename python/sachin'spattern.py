def call(i):
    for j in range(2,i):
        if(i%j==0):
            return(0)
    return(1)
c=int(input())
for i in range(2,c//2):
    if(c%i==0):
        if(call(i)):
            print(i)
