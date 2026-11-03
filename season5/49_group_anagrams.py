from typing import List, Set, Dict, Optional

null = None


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """
        Let N be number of words
        Let M be average length of each word
        => N * M
        """

        anagramMap: dict[tuple, list[str]] = {}

        # key: (0,0,0,0,0,0,0,0,0,0,0) <- 26 of them

        a = ord("a")

        # N loops
        for s in strs:
            key = [0] * 26

            # M loops
            for c in s:
                index = ord(c) - a
                # ord(c) is ascii number of c, a is ascii of 'a'
                # ex: for 'c', ord('c') 98, 98 - 96 -> 2, since 'c' is the 3rd letter
                key[index] += 1

            # convert tuple is O(M)
            key = tuple(key)

            # O(1)
            if key in anagramMap:
                anagramMap[key].append(s)
            else:
                anagramMap[key] = [s]

        # O(N)
        return list(anagramMap.values())


if __name__ == "__main__":
    o = Solution()

    print(o.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat", "create"]))
