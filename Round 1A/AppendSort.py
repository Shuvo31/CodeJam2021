def modified(a, b):
    thisCount = 0
    
    if b > a:
        return b,thisCount
    working = b
    lendiff = len(str(a)) - len(str(b))
    working = int(str(b) + "0"*lendiff)
    thisCount += lendiff
    if working > a:
        return working, thisCount
    
    offset = a - working
    if (offset >= (10**lendiff - 1)):
        working = int(str(working) + "0")
        thisCount += 1
    else:
        working += offset + 1
    return working, thisCount
T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    nums = list(map(int, input().split()))
    count = 0
    for i in range(1, n):
        nums[i], thisCount = modified(nums[i-1], nums[i])
        count += thisCount
    print("Case #{}: {}".format(test_case, count))