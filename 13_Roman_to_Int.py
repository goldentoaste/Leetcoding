class Solution(object):
    def romanToInt(self, s: str):
        """
        I             1
        V             5
        X             10
        L             50
        C             100
        D             500
        M             1000
        """

        table = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        for i in range(len(s)):
            cur = s[i]
            if i > 0:
                prev = s[i - 1]
                if table[prev] < table[cur]:
                    total += table[cur] - table[prev]
                    continue

            if i < len(s) - 1:
                nex = s[i + 1]
                if table[cur] >= table[nex]:
                    total += table[cur]
            else:
                total += table[cur]
        return total


if __name__ == "__main__":
    print(Solution().romanToInt(("MCMXCIV")))
