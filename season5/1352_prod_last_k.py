from typing import List, Set, Dict, Optional
null = None




class ProductOfNumbers:
    '''
    Use prefix sum technique, so that we can make continuous range query. 
    The problem description assumes all inputs are 32bit integers and does not overflow.
    So we assume multiplications and division is stable.

    Actually 0 is a special case.
    Since we only care about last k numbers, products before encountering 0s are practically 0, so we can wipe 
    mem when 0 is seen.
    '''

    def __init__(self):

        # Semantically, self.mem[i] is the product of all numbers in the range of [0, i), i is 0 index, not inclusive.
        self.mem = [1]

    def add(self, num: int) -> None:
        if num==0:
            self.mem.clear()
            self.mem.append(1)
        else:
            self.mem.append(self.mem[-1] * num)

    def getProduct(self, k: int) -> int:
        if k > len(self.mem) - 1:return 0

        return self.mem[-1] // self.mem[-k - 1] # minus 1 to include the kth number. 

if __name__ == "__main__":
    o = ProductOfNumbers()
    o.add(3)     
    o.add(0)     
    o.add(2)     
    o.add(5)     
    o.add(4)     
    print(o.getProduct(2))
