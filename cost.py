A,x,B = map(int,input().split())

cases = [[x,0]]

min_c = 0
while cases:
    case = cases.pop()
    n,c = case[:]

    if n==0:
        if c<min_c or min_c ==0:
            min_c = c 
        continue
    if n%2==0:
        if c+B<=min_c or min_c==0:
            new = [n//2,c+B]
            cases.append(new)
            #cases.insert(0,new)
    else:
        if c+B+A<=min_c or min_c==0:
            new = [(n-1)//2,c+A+B]
            cases.append(new)
            new = [(n+1)//2,c+A+B]
            cases.append(new)
    if (n//2)*A<B:
        new = [n-1,c+A]
        cases.append(new)

print(min_c)





