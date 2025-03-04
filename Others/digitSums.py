import matplotlib.pyplot as plt
def digitSum(n:int):
    return sum([int(d) for d in str(n)])

def digitSumToN(n:int):

    for i in range(n):
        yield digitSum(i)

plt.plot(list(digitSumToN(100000)))
plt.show()