from typing import List, Set, Dict, Optional

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        counter = [0] * 26

        for c in s:
            counter[ord(c) - 97] += 1
        
        ranked = sorted([(val, index )for index, val in enumerate(counter)], reverse=True)


        low = 0
        high = len(s)
        while ranked and ranked[-1][0] < k:
            # reduce size of scope until s[low: high] matches criteria
            count, char = ranked.pop()
            char = chr(char)


            for i in range(count):
                
                low_cand = s.find(char, low, high)
                high_cand = s.rfind(char, low, high)

                low_dist = low_cand- low


        

        return high - low




if __name__ == "__main__":
    o = Solution()
    print(o.longestSubstring("ababbc", 2)) # expect 5, because ababb