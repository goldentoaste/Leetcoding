class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        count = 0 
        while n != 0:
            if n & 1:
                count += 1
            n //= 2
        return count
    
    
if __name__ == "__main__":
    o = Solution()
    print(o.hammingWeight(5))