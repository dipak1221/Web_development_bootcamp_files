import math
for i in range(int(input())):
    h,c,t=map(int,input().split())
    x=0
    y=0
    m=t
    while(True):
        x+=1
        if abs(t-(h*x+c*y)/(x+y))<0.5:
            m=abs(t-(h*x+c*y)/(x+y))
            break
        y+=1
        
        if abs(t-(h*x+c*y)/(x+y))<0.5:
            m=abs(t-(h*x+c*y)/(x+y))
            break

    print(x+y)
            
