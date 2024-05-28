class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) != len(nums)



if __name__ == "__main__":
    o = Solution()
    print(o.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
