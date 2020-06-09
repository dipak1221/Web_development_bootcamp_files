for i in range(int(input())):
    n=int(input())
    if(n==1):
        print(0)
    else:
        sum=0
        for ii in range(1,(n//2)+1):
            sum+=(2**(ii+2))*ii
        print(sum)
            
