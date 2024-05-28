def solution(N, P, Q):
    # Implement your solution here

    cache = arrayF(N)
    sums = []
    total = 0
    for i in range(N+1):
        total+= 1 * isSemiPrime(i,cache) 
        sums.append(total)
    out = []
    for low, high in zip(P, Q):

        out.append(sums[high]-sums[low-1])

    
   
    return out


def arrayF(n):
    F = [0] * (n + 1)
    i = 2
    while i * i <= n:
        if F[i] == 0:
            k = i * i
            while k <= n:
                if F[k] == 0:
                    F[k] = i
                k += i
        i += 1
    return F


def isSemiPrime(x, cache):

    if cache[x] == 0:
        return False

    temp = x // cache[x]

    return cache[temp] == 0


print(solution(26, [1, 4, 16], [26, 10, 20]))
