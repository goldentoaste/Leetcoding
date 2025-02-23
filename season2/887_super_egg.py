class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        
        # K is how many eggs left, N is how many floors not tried yet.
        
        mem = dict()
        
        # do binary search on floors
        def dp(K, N):
            if K == 1:
                return N # if only 1 egg is left, need to try every floor
            if N == 0:
                return 0 # no floors left, no tries are needed.          
            if (K, N) in mem:
                return mem[(K, N)]
            
            # note that for any number of eggs, more floors = maybe more tries, not less tries.
            # so binary search on floors is applicable.
            
            low = 1
            high = N
            
            actual = float("inf")
            while low <= high:
                mid = (low + high) // 2 
                
                # lets pretend we dropped it at <mid> floor
                
                broken = dp(K - 1, mid - 1) # if egg breaks, we lose 1 egg, also the right floor must be below.
                good = dp(K, N - mid) # egg no break, keep the egg and search lower half of building
                
                # since we need to "be confident", lets pretends we always take which ever is larger.                
                if broken > good:
                    high = mid - 1
                    actual = min(actual, broken + 1)
                else:
                    low = mid + 1
                    actual = min(actual, good + 1) 
            mem[(K, N)] = actual
            return actual
        
        return dp(k, n)
        
if __name__ == "__main__":
    o = Solution()
    print(o.superEggDrop(2, 6)) #expect 3