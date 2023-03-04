# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    out = []

    factorCache = arrayF(len(A) * 2)
    
    for num in A:
        out.append(sum((1 for x in A if x not in factors(num, factorCache))))
    return out

def arrayF(n):
    F = [0] * (n+1)
    i = 2
    while i * i <= n:
        if F[i] == 0:
            k = i * i
            while k <= n:
                if F[k] == 0:
                    F[k] = i
                k+=i
        i += 1
    return F

def factors(x, F):

    primes = {1, x}

    while F[x] >0:
        primes.add(F[x])
        x //= F[x]

    primes.add(x)
    return primes


print(solution([3, 1, 2, 3, 6]))