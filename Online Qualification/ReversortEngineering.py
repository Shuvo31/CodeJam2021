def createList(a):
    l = []
    for i in range(1,a+1):
        l.append(i)
    return l 

def operationList(a, b):
    if b < a-1:
        return []
    l = []
    t = 0 
    c = 1
    for i in range(a-1, 0, -1):
        c += 1

        if t+c+i-1 >= b:
            r = b-t-i+1
            l.append(r)
            for k in range(i-1):
                l.append(1)
            t = b
            break

        t += c 
        l.append(c)
    if t<b:
        return []
    return l

def orate(l, opeL):
    length = len(opeL)
    for i in range(length):
        t = len(l)-(i+2)
        sp = t+opeL[i]
        l = l[:t]+ list(reversed(l[t:sp])) + l[sp:]
    return l 

def solve():
    inp= input().split()
    a = int(inp[0])
    b = int(inp[1])
    l = createList(a)
    opeL = operationList(a,b)
    l = orate(l, opeL)
    result = " "
    if opeL:
        for item in l:
            result += str(item)+ " "
    else:
        result =" IMPOSSIBLE"
    print("Case #"+str(i+1)+": "+ str(result))

for i in range(int(input())):
    solve()