a,b,c,x,y=map(int,input().split())
ab=a+b
d=[10**9]
if ab < 2*c:
    print(a*x+b*y)
else:
    #abピザをmax(x,y)コ買う
    #余分に買う
    ans1=max(x,y)*(2*c)
    #abピザをmin(x,y)コ買う+不足分を買う
    if x<y:
        tmp=x*(2*c)
        y=y-x
        rem=y*b
        d.append(tmp+rem)
    elif y<x:
        tmp=y*(2*c)
        x=x-y
        rem=x*a
        d.append(tmp+rem)
    ans2=min(d)
    print(min(ans1,ans2))
