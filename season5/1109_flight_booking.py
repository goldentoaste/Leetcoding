from typing import List, Set, Dict, Optional

null = None


class Solution:
    def corpFlightBookings(self, bookings: list[list[int]], n: int) -> list[int]:
        '''
        https://leetcode.com/problems/corporate-flight-bookings/description/

        This problem makes use of the diff array technique, which is good for O(1) modification of a range

        1. Make precomputed data structure of each element diffed with prev:
            * arr = [2, 5, 1, 8, 2, 7] ->
            * diff = [2, 3, -4, 7, -6, 5]
        2. Diff tracks the change to get from 1 number to the next
        3. arr[i] = arr[i - 1] + diff[i], since diff[i] = arr[i] - arr[i - 1]
            => arr[i] = arr[i - 2] + diff[i - 1] + diff[i]...
            => a increase in diff affects all subsequent numbers
        4. So, to modify a range [a, b) do
            * diff[a] += x
            * diff[b] -= x
        5. Derive modified array based on formula arr[i] = arr[i - 1] + diff[i]
            * Note that arr[0] = diff[0] and the reoccurrence relation does no apply. (Or we can pad arr with leading 0)
        '''

        diff = [0] * n
        out = []
        for start, end, amt in bookings:
            diff[start - 1] += amt
            if end < n:
                diff[end] -= amt

        out.append(diff[0])
        for d in diff[1:]:
            out.append(out[-1] + d)

        return out


if __name__ == "__main__":
    o = Solution()

    print(o.corpFlightBookings(bookings= [[1,2,10],[2,3,20],[2,5,25]], n = 5)) # [10,55,45,25,25]
