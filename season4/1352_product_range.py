from typing import Dict, List, Optional, Set


class ProductOfNumbers:

    def __init__(self):
        self.mem = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.mem = [0] * (len(self.mem) + 1)
        elif self.mem[-1] == 0:
            self.mem.append(num)
        else:
            self.mem.append(self.mem[-1] * num)

    def getProduct(self, k: int) -> int:
        if self.mem[-k] == 0:
            return 0
        if  self.mem[-k - 1] == 0:
            return self.mem[-1]
        return self.mem[-1] // self.mem[-k - 1]


if __name__ == "__main__":
    o = ProductOfNumbers()
    o.add(3)
    o.add(0)
    o.add(2)
    o.add(5)
    o.add(4)
    print(o.getProduct(4))
