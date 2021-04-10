import copy
import math

def reduced_primesets(primes):
    threshold = 0
    for i in primes:
        threshold += i * primes[i]

    flop = True
    subsets_1 = [(1, 0)]
    subsets_2 = []

    for prime in primes:
        primecount = primes[prime]

        if flop:
            for prod, thisSum in subsets_1:
                max_of_this_prime = int(math.log(threshold / prod, prime))
                bound = min(max_of_this_prime + 1, primecount + 1)
                for i in range(bound):
                    subsets_2.append((prod*(prime**i), thisSum+(prime*(primecount-i))))
            subsets_1 = []
        else:
            for prod, thisSum in subsets_2:
                max_of_this_prime = int(math.log(threshold / prod, prime))
                bound = min(max_of_this_prime + 1, primecount + 1)
                for i in range(bound):
                    subsets_1.append((prod*(prime**i), thisSum+(prime*(primecount-i))))
            subsets_2 = []

        flop = not flop

    if flop:
        return subsets_1
    return subsets_2

T = int(input())

for test_case in range(1, T+1):
    m = int(input())
    primes = {}
    for _ in range(m):
        p,n = map(int, input().split())
        primes[p] = n

    ans = 0

    solutionsets = reduced_primesets(primes)
    for p,q in solutionsets:
        if p == q:
            ans = max(ans, p)

    print("Case #{}: {}".format(test_case, ans))