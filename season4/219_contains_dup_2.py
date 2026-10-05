from typing import Dict, List, Optional, Set

null = None


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        gameplan: sliding window, keep number within this window.
        If there are duplicate, return true
        """
        mem = set()

        left = 0
        for right, n in enumerate(nums):
            if n in mem:
                return True

            mem.add(n)
            if right >= k:
                # slide window
                mem.remove(nums[left])
                left += 1

        return False


if __name__ == "__main__":
    o = Solution()
    print(o.containsNearbyDuplicate([1, 1], 2))  # true
    print(o.containsNearbyDuplicate(nums=[1, 2, 3, 1], k=3))  # true
    print(o.containsNearbyDuplicate(nums=[1, 0, 1, 1], k=1))  # true
    print(o.containsNearbyDuplicate(nums=[1, 2, 3, 1, 2, 3], k=2))  # false
