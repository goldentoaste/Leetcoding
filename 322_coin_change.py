from typing import List, Set, Dict, Optional



class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        change(n) = 
        -> (if n <=0) 0
        -> for c in coins: change(n - c) if n >= c
        
        '''
        
        mem = [-2] * (amount + 1)
        mem[0] = 0
        
        
        def change(amt:int):
            
            if mem[amt] != -2:
                return mem[amt]
            
            if amt <= 0:
                return 0
            
            val = float('inf')
            changeFound = False
            for c in coins:
                if c == amt:
                    mem[amt] = 1
                    return 1 # exact change
                
                if c > amt:
                    continue # change using this coin is not possible
                
                val_c = change(amt - c)
                
                if val_c == -1:
                    continue # solution if this coin is chosen
                
                val = min(val, val_c)
                changeFound = True
            
            if not changeFound:
                mem[amt] = -1
                return -1
            else:
                mem[amt] = val + 1
                return val + 1
        change(amount)

        return mem[-1]


if __name__ == "__main__":
    o = Solution()
    print(o.coinChange([1, 2, 5], 11))
    print(o.coinChange([2], 3))
    print(o.coinChange([1], 0))

    print(o.coinChange([1], 1))
    
    print(o.coinChange([186,419,83,408], 6249))