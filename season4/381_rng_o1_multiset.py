from collections import defaultdict
from math import floor
from random import random


class RandomizedCollection:

    def __init__(self):
        # maps the value onto a set of array index
        self.indexMap = defaultdict(set)

        # array to store actual data
        # vals is added or removed, must be done in a way to only affect const # of indices
        self.data = []

    def insert(self, val: int) -> bool:
        self.data.append(val)
        self.indexMap[val].add(len(self.data) - 1)

        # print("debug", self.indexMap[val], self.data)
        return len(self.indexMap[val]) == 1

    def remove(self, val: int) -> bool:
        if val not in self.indexMap or len(self.indexMap[val]) == 0:
            return False


        # pop tail
        tail = self.data[-1]
        self.indexMap[tail].remove(len(self.data) - 1)

        # special case, end is remove target
        if val == tail:
            self.data.pop()
            return len(self.indexMap[val]) >= 0


        # remove idx record
        valIdx = self.indexMap[val].pop()

        # overwrite with tail to remove
        self.data[valIdx] = tail
        self.indexMap[tail].add(valIdx)
        self.data.pop()  # remove old tail

        return len(self.indexMap[val]) >= 0

    def getRandom(self) -> int:
        randIdx = floor(random() * len(self.data))
        return self.data[randIdx]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


if __name__ == "__main__":
    o = RandomizedCollection()
    print(o.insert(1))
    print(o.remove(2))
    print(o.insert(2))
    print(o.getRandom())
    print(o.remove(1))
    print(o.insert(2))
    print(o.getRandom())
