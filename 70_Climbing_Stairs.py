from typing import List, Set, Dict, Optional


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        last = [[1]]
        current = []

        for i in range(1, n):
            for combo in last:
                # try inserting 1
                for j in range(len(combo)):
                    if combo[j] == 2:
                        temp = combo.copy()
                        temp.insert(j, 1)
                        current.append(temp)
                print(current)
                current.append(combo.copy() + [1])

                # try replace 1 with 2
                for j in range(len(combo)):
                    if combo[j] == 1:
                        temp = combo.copy()
                        temp[j] = 2
                        current.append(temp)
            last = current
            current = []

        return len(last)


if __name__ == "__main__":
    o = Solution()

    print(o.climbStairs(3))
