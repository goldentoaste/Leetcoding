from typing import Dict, List, Optional, Set

null = None


class Solution:

    def better():
        '''
        alternatively, its also acceptable to
        1. calc total area of all squares combined, divide by 2 to find the target.
        2. sort the list of squares.
        3. Repeat the following until goal is exceeded:
            -1. record y at each step
            a. include a square
            b. include all squares with the prev square's y
        4. binary search within a more limited range, with a smaller search space.

        This is harder to implement than the submission, but should have a better performance and complexity.
        '''
        pass

    def separateSquares(self, squares: List[List[int]]) -> float:
        """
        squares: [(x, y, l),...]

        Ideas: use bin search.

        Define a function f(y) as the difference of area above and below y.
        when y is -inf, all squares are above, f(y) is positive.
        as y grows f(y) can only decrease.
        f(y) is monotonic.
        bin search on y such that f(y) = 0 (as close epsilon to 0)
        Time complexity so far is lg(steps) * O(f)

        Note, although f(y) is monotonic, it is not strictly monotone decreasing.
        Remember to search for min y value.

        how to implement f(y)?
            + it takes O(n) to scan each square...
            + can sort the list of sqrs by y?
            + for any y, how to find all squares colliding with it?
        """

        def area(y):
            """
            given y, return area above - below.

            This is a O(n) ops, how calc this faster?
            """

            above = 0
            below = 0

            for _, _y, length in squares:
                if _y >= y:
                    above += length * length  # entirely above
                elif _y + length <= y:
                    below += length * length  # entire below
                else:  # square collides with y
                    lower = y - _y
                    below += lower * length
                    above += (length - lower) * length
            return above - below

        low = float('inf')
        high = float('-inf')
        epsilon = 10 ** (-5)

        for _, _y, length in squares:
            low = min(low, _y)
            high = max(high, _y + length)

        while True:
            y = ((high - low) / 2 )+ low
            diff = area(y)
            if diff > epsilon:
                # above > below
                low = y
            elif diff < -epsilon:
                # below > above, try higher y
                high = y
            else:
                # diff is within epsilon to 0
                # try a lower y still
                high = y

            if (high - low) < epsilon:
                # search has converged within epsilon. We are done.
                return ((high - low) / 2 )+ low




if __name__ == "__main__":
    o = Solution()
    print(o.separateSquares([[0, 0, 2], [1, 1, 1]]))
