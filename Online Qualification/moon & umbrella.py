def moon(p,a,b):
    fee = 0 
    fee =p.count("CJ")*a + p.count("JC")*b
    return fee
def solve():
    t= input().split()
    a = int(inp[0])
    b = int(inp[1])
    p = t[2]
    fee = moon(p,a,b)
    length = len(p)
    i = 0
    while i < length:
        m =""
        if i > 0 and p[i] == "?":
            m = p[i-1] 
        while p[i] == "?":
            if i < (length-1):
                i = i+1

            else:
                break
       
        f = m + p[i]
        if f == "CJ":
                fee += a 
        elif f == "JC":
                fee += b
        i+=1

    print("Case #"+str(u+1)+": "+ str(fee))

for u in range(int(input())):
    solve()