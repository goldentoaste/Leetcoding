
from typing import List, Set, Dict, Optional
null = None

class Solution:
    def lengthLongestPath(self, s: str) -> int:
        lines = s.split('\n')

        # (tabcount, strLength)
        items = [(l.count('\t'), len(l) - l.count('\t'), l.find('.') >= 0) for l in lines]
        print(items)
        depth = -1
        length = 0
        maxLength = 0

        stack = []

        for item in items:
            d, l, isFile = item
            if d > depth: # deeper
                length += l
            elif d == depth: # same depth
                _, lastLength, __ = stack.pop()
                length -= lastLength
                length += l
            elif d < depth:
                while stack and d <= stack[-1][0]:
                    lastDepth, lastLength,_ = stack.pop()
                    depth = lastDepth
                    length -= lastLength
                length += l

            depth = d
            stack.append(item)
            if isFile:
                maxLength = max(length + d, maxLength)

        return maxLength

if __name__ == "__main__":
    o = Solution()
    # expect 32
    print(o.lengthLongestPath("a\n\tb.txt\na2\n\tb2.txt"))
    # print(o.lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))