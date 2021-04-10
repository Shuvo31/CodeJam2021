reverse = int(input())  
for i in range(1, reverse + 1):
    a = int(input())
    b = list(map(int, input().split()))
    out = 0
    for index in range(a-1):
        min_index = b.index(min(b[index:a]))
        b[index: min_index + 1] = reversed(b[index: min_index + 1])
        out += (min_index) - (index) + 1
    print("Case #{}: {}".format(i, out))