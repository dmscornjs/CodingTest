while True:
    a = input()
    al = []
    r = "yes"
    if a == '.':
        break
    for i in a:
        if i == '(':
            al.append('c')
            
        elif i == ')':
            try:
                z = al.pop(-1)
            except:
                r = "no"
            if z != 'c':
                r = "no"
                
        elif i=='[':
            al.append('d')
            
        elif i ==']':
            try:
                z = al.pop(-1)
            except:
                r = "no"
            if z != 'd':
                r = "no"             
    
    if len(al) != 0:
        print("no")
        
    else:
        print(r)
            
