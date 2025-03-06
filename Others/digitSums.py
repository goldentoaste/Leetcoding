import math
from timeit import timeit


def digitSum(n: int):
    return sum([int(d) for d in str(n)])


def digitSumN(n: int):
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total


# wiki https://en.wikipedia.org/wiki/Digit_sum
def wikiDigitSum(n: int, q: int):
    """
    how many number with n digits has sum of q

    worse case: O(10 ** n)?
    """

    if n == 1:
        return 1

    if q > math.ceil((9 * n) / 2):
        return wikiDigitSum(n, 9 * n - q + 1)

    total = 0
    # otherwise
    for i in range(max(q - 9, 1), q + 1):  # inclusive q
        total += wikiDigitSum(n - 1, i)

    return total


memo = dict()


def wikiDigitSumWithMemo(n: int, q: int):
    """
    with memo, O(n * q)
    """
    if (n, q) in memo:
        return memo[(n, q)]

    if n == 1:
        return 1

    if q > math.ceil((9 * n) / 2):
        return wikiDigitSumWithMemo(n, 9 * n - q + 1)

    total = 0
    # otherwise
    for i in range(max(q - 9, 1), q + 1):  # inclusive q
        total += wikiDigitSumWithMemo(n - 1, i)

    memo[(n, q)] = total
    return total


def naiveDigitSum(n: int, q: int):

    total = 0
    for i in range(10 ** (n - 1), 10**n):
        s = digitSumN(i)
        if s == q:
            total += 1

    return total


print(f"wiki sum: {wikiDigitSum(6, 30)}")
print(f"wiki memo sum: {wikiDigitSumWithMemo(6, 30)}")
print(f"naive sum: {naiveDigitSum(6, 30)}")


print(
    timeit(
        "wikiDigitSum(6, 30)",
        """
import math
            
def wikiDigitSum(n:int, q:int):
    if n == 1:
        return 1
    
    if q > math.ceil((9 * n) / 2):
        return wikiDigitSum(n, 9 * n - q + 1)
    
    total = 0
    # otherwise
    for i in range(max(q - 9, 1), q + 1): # inclusive q
        total += wikiDigitSum(n - 1, i)
    
    return total""",
        number=100,
    )
)


# memo
print(
    timeit(
        "wikiDigitSumWithMemo(6, 30)",
        """
import math
            
memo = dict()
def wikiDigitSumWithMemo(n:int, q:int):
    if (n, q) in memo:
        return memo[(n,q)]

    if n == 1:
        return 1
    
    if q > math.ceil((9 * n) / 2):
        return wikiDigitSumWithMemo(n, 9 * n - q + 1)
    
    total = 0
    # otherwise
    for i in range(max(q - 9, 1), q + 1): # inclusive q
        total += wikiDigitSumWithMemo(n - 1, i)
    
    memo[(n, q)] = total
    return total""",
        number=100,
    )
)


print(
    timeit(
        "naiveDigitSum(6, 30)",
        """
import math
def digitSumN(n:int):
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total

def naiveDigitSum(n:int, q:int):

    total = 0
    for i in range(10 ** (n - 1), 10 ** n):
        s = digitSumN(i)
        if s == q:
            total += 1

    return total
""",
        number=100,
    )
)
