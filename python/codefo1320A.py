n=int(input())
l=[0]*n
i2=i3=i5=0
next_2=2
next_5=5


for i in range(1,n):
    l[i]=min(next_2,next_5)

    if next_2==l[i]:
        i2+=1
        next_2=l[i2]*10+2
    if next_5==l[i]:
        i5+=1
        next_5=l[i5]*10+5

print(l[1:])
