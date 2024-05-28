class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        # each i, j, is least operations for first j chars of word2 to each first i char of word1.
        dp = [[0] * (len(word2) + 1) for i in range(len(word1) + 1)]  # TODO optimization: only include current and prev row during loop

        # base case
        for i in range(len(word1) + 1):
            dp[i][0] = i  # if j is 0 chars,  then i operations are neeed to i chars (addition)

        for j in range(len(word2) + 1):
            dp[0][j] = j  # if target is 0 chars, then j ops are need to reach 0 chars (deletes)

        # compute each position of the dp table

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:  # note that 0th position is empty string, so i and j are offset by 1.
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i][j - 1] + 1,  # add char to word1
                        dp[i - 1][j] + 1,  # delete a char from word1
                        dp[i - 1][j - 1] + 1,  # replace a char from word1 (add and delete at the same time)
                    )
        return dp[len(word1)][len(word2)]


if __name__ == "__main__":
    o = Solution()

    print(o.minDistance("", "a"))  # expect 5
