from collections import deque
from typing import List, Set, Dict, Optional


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        def increment(val, pos, by):
            return val[:pos] + str((int(val[pos]) + by) % 10) + val[pos + 1 :]

        if target == "0000":
            return 0

        mem = set(deadends)  # avoid combination already branched from
        
        if '0000' in mem or target in mem:
            return -1
        
        q = deque(["0000"])
        moves = -1

        while q:
            moves += 1
            for _ in range(len(q)):
                item = q.popleft()
                if item == target:
                    return moves

                for i in range(4):
                    up = increment(item, i, 1)
                    if up not in mem:
                        q.append(up)
                        mem.add(up)
                    down = increment(item, i, -1)
                    if down not in mem:
                        q.append(down)
                        mem.add(down)

        return -1


if __name__ == "__main__":
    o = Solution()
    # print(o.openLock(["0201", "0101", "0102", "1212", "2002"], "0202"))
    print(o.openLock(["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], "8888"))
    # print(o.openLock(["8888"], "0009"))
