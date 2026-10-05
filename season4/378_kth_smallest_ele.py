from typing import List, Set, Dict, Optional
null = None

import heapq as hq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        '''
        treat each row as a sorted list, then apply algo to merge n sorted list.

        intuition, when merging lists, the next smallest could could be the head 
        of the any of the sorted lists. Use a heap to track the smallest head.

        Complexity, the heap's max size is about k, since we are only looking for 
        the top k nums. Each time a new number is added takes log(k)

        so kLog(k) in total.
        '''
        
        queue = [(matrix[i][0], i, 0) for i in range(len(matrix))]
        hq.heapify(queue)

        while k > 0:
            k -= 1
            val, row, index = hq.heappop(queue)
            if k == 0:
                return val
            
            # append next item in this current row
            if index < len(matrix[row]) - 1:
                hq.heappush(queue, (matrix[row][index + 1], row, index + 1))
            
        





if __name__ == "__main__":
    o = Solution()
    mat = [
        [ 1,  5,  9],
        [10, 11, 13],
        [12, 13, 15]
    ]

    print(o.kthSmallest(mat, 8))