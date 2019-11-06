T = int(input())

for t in range(T):
    N, M, S, Q = map(int, input().split())
    p = list(map(int, input().split()))
    p.append(2*N + 1) #to the places append 2*last place +1
    c = [-1 for i in range(2*N)] #flowers assigned to which sprinkler?, the previous one
    for i in range(len(p) - 1):
        for j in range(p[i], p[i + 1]):
            c[j - 1] = i
    r = 10 ** 16
    me = -1
    sprink_pos = []
    # print c
    for e in range(N):
        rr = e * Q
        pos = e
        v = []
        print('e:', e)
        if c[pos] == -1:
            rr = r
            pos = N
        while pos < N + e:
            print('pos:', pos,c[pos], p[c[pos]])
            v.append(str(p[c[pos]])) #the sprinkler position which is supposed to cover this 
            if pos >= p[c[pos]] + 2 * e: #if current flower is far away from current sprinkler
                rr = r
                break
            pos = p[c[pos]] +2*e #else update the position
            rr += S #else the cost is this much
        if rr < r:
            sprink_pos = v
            me = e
            r = rr
        # print 'r:', r
    print(len(sprink_pos), me) #number of sprinklers and meters
    print(' '.join(sprink_pos))
        