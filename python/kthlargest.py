for i in range(int(input())):
    s=input()
    n=int(input())
    d={}
    for i in s:
        if s.count(i) not in d:
            d[s.count(i)]=[i]
        else:
            d[s.count(i)].append(i)

    l=list(d.keys())
    l.sort(reverse=True)
    
    if (len(d)<n):
        print(-1)
    else:
        print(min(d[l[n-1]]))
        
