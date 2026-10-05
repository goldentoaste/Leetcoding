from typing import List, Set, Dict, Optional

null = None


class Solution:

    def minWaitTime(self, music: list[int], k):
        """
        Music is array of song's length.
        Play in sequence
        Remove k songs so the delay is minimized.

        https://labuladong.online/en/problem/eleme-music-queue/description/
        """

        for i in range(k):
            peak = -1
            peakIdx = -1
            acc = 0
            for j in range(len(music)):
                after = music[j] * (len(music) - j - 1)


                if after > peak:
                    peak = after
                    peakIdx = j

                if acc > peak:
                    peak = acc
                    peakIdx = j

                acc += music[j]
            music.pop(peakIdx)
        return sum((music[i] * (len(music) - i - 1) for i in range(len(music))))


if __name__ == "__main__":
    o = Solution()
    print(o.musicQueue([3, 1, 4, 2], k=2))
