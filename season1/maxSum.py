

from typing import List



def dpSum(arr : List[int]):
    
    # find the max sum of a sub array using dynamic programming

    # each position (i) in mem is the max val of any sub arr that ends at i
    mem = [0] * len(arr)
    mem[0] = arr[0]

    for index, num in enumerate(arr[1:], 1):

        mem[index] = max(mem[index - 1] + num, num)


    return max(mem)

def kadaneAlgo(arr):

    maxSoFar = arr[0]
    prev = arr[0]
    for num in arr[1:]:
        prev = max(prev + num, num)
        maxSoFar = max(prev, maxSoFar)

    return maxSoFar
if __name__ == '__main__':

    print(kadaneAlgo([3, 2, -6,  4, 0]))