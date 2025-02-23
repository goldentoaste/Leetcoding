class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        mem = set()

        low, high = 0, 0
        out = 0
        while high < len(s):
            cur = s[high]

            while cur in mem:
                mem.remove(s[low])
                low += 1

            mem.add(cur)

            if len(mem) > out:
                out = len(mem)
            high += 1

        return out


if __name__ == "__main__":
    o = Solution()

    print(o.lengthOfLongestSubstring("pwwkew"))  # expect 3
