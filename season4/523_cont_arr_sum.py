from typing import List, Set, Dict, Optional



class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return True

        counter = 0
        mem = dict()
        zeros = 0

        for idx, n in enumerate(nums):
            counter += n
            if n == 0:
                zeros += 1
                if zeros >= 2:
                    return True
            else:
                zeros = 0

            if counter not in mem:
                mem[counter] = idx

            if counter < k:
                continue

            remainder = counter % k
            if remainder == 0 and idx >= 1:
                return True

            if remainder in mem and mem[remainder] < idx - 1:
                return True

        return False



if __name__ == "__main__":
    o = Solution()
    print(o.checkSubarraySum([5, 0, 3], 5))

    # print(o.checkSubarraySum([1], 1))
    # print(o.checkSubarraySum([0], 1))
    # print(o.checkSubarraySum([5, 0,0], 3))
    # print(o.checkSubarraySum([23,2,4,6,7],6))
    # print(o.checkSubarraySum([23,2,6,4,7],6))
    # print(o.checkSubarraySum([23,2,6, 4,7],13))

