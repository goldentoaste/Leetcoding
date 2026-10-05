from typing import List, Set, Dict, Optional




class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        '''
        remove numbers from 2 ends of nums to reduce x to zero

        observation, this is the same as the question of, finding the longest subarr that sums up
        to Total - x

        using this fact, we can use a sliding window technique to find longest sub arr
        '''
        maxMatchingLength = 0
        target = sum(nums) - x

        if target < 1:
            return -1


        low = 0
        curSum = 0
        for high in range(len(nums)):
            curSum += nums[high]

            while curSum > target:
                curSum -= nums[low]
                low += 1

            if curSum == target:
                maxMatchingLength = max(maxMatchingLength, high - low + 1)

        if maxMatchingLength == 0 :
            return -1
        return len(nums) - maxMatchingLength

if __name__ == "__main__":
    o = Solution()
    print(o.minOperations([3,2,20,1,1,3], 10))