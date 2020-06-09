def call(a):
    c=0
    j=2
    while(1):
        for i in range(1,j):
            c=c+1
            if(c==a):
                return(i)
        j+=1
a=int(input())
c=call(a)
print(c)
