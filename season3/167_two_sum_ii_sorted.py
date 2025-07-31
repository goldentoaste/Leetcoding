from typing import Dict, List, Optional, Set


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        low, high = 0, len(numbers) - 1
        
        while low < high:
            total = numbers[low] + numbers[high]
            
            if total < target:
                low += 1
            elif total > target:
                high -=1
            else:
                break
        
        return [low + 1, high + 1]


if __name__ == "__main__":
    o = Solution()
    print(o.twoSum([2,7,11,15], 9)) # expect [1, 2]