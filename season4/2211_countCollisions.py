


from typing import List, Set, Dict, Optional
null = None


class Solution:
    def countCollisions(self, directions: str) -> int:
        '''
        thing of right as opening backets and stationary and left as closing.
        '''

        mem = []
        count = 0
        for d in directions:
            if not mem:
                mem.append(d)
                continue
            if d == "R":
                mem.append(d)
                continue

            if d == "L":
                last = mem.pop()
                if last in ('R', 'S'):
                    if last == 'R':
                        count += 2
                    if last == 'S':
                        count += 1
                    # collision has occured, the 2 crashed cars becomes stationary
                    mem.append('S')

            if d == 'S' or (mem and mem[-1] == 'S'):
                while mem:
                    last = mem.pop()
                    if last == "R":
                        count += 1
                mem.append('S')
        return count


if __name__ == "__main__":
    o = Solution()
    print(o.countCollisions("RLRSLL")) # expect 5
    print(o.countCollisions('LLRLRLLSLRLLSLSSSS')) # expect 10
