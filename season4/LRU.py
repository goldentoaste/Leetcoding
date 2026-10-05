

'''
LRU cache

design data structure to hold /fixedlimit # items, 
map that keeps limit items, discard least recently used key\
'''

from collections import deque

class LRUCache:
    def __init__(self, length):
        self.length = length
        self.mem = {}
        self.queue = deque()

    def get(self,key:int):
        if key not in self.mem:
            return -1
        self.queue.remove(key)
        self.queue.append(key)
        return self.mem[key]

    def put(self, key:int, value:int):
        self.mem[key] = value
        if len(self.mem) > self.length:
            lastKey = self.queue.popleft()
            self.mem.pop(lastKey)
        else:
            if key in self.queue:
                self.queue.remove(key)
            self.queue.append(key)



test = LRUCache(4)

print("key not found:",  test.get(5) == -1) # expect -1

test.put(0, 111)
test.put(3, 456)
test.put(2, 789)

print("cases for getting values:")
print(test.get(0) == 111) 
print(test.get(2) == 789) 

test.put(5, 222)
test.put(6, 222)

print("exceeding limit, remove oldest", test.get(3) == -1)

test.put(0, 123)
print("put test:", test.get(0) == 123)
test.put(0, 333)
print("overwrite test: ", test.get(0) == 333)
