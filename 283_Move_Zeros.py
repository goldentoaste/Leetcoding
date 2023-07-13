class Solution(object):
    def moveZeroes(self, nums: list):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        zeros = 0
        for index, num in reversed(list(enumerate(nums))):
            if not num:
                nums.pop(index)
                zeros+=1
                
                
        nums.extend([0]*zeros)

if __name__ == "__main__":
    o = Solution()
    l = [1, 2, 5,0,6,0,7,999,0,2,3]
    o.moveZeroes(l)
    print(l)
