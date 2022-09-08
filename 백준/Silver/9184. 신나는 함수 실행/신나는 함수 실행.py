def w(a,b,c):
    try:
        return dic[(a,b,c)]
    except:
        if (a<=0) or (b<=0) or (c<=0):
            return 1
        if (a>20) or (b>20) or (c>20): 
            return w(20, 20, 20)
        if (a<b) and (b<c):
            dic[(a,b,c)] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c-1)
            return dic[(a,b,c)]
        else:
            dic[(a,b,c)] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
            return dic[(a,b,c)]

dic = {}
while True:
    a, b, c = map(int, input().split())
    if a==b==c==-1:
        break
    print("w({0}, {1}, {2}) =".format(a,b,c,),w(a,b,c))