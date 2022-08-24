a, b, c = map(int, input().split())
if b==c:
    print(-1)
else:    
    x=int(a/(c-b))
    if x<0:
        print(-1)
    elif x==0:
        if c>b:
            print(1)
        else:
            print(-1)
    else:
        print(x+1)
