class Solution(object):
    def countBits(self, n: int):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]

        powers = []
        index = 0
        out = [0, 1]
        while True:
            num = 2**index
            powers.append(index)
            if num >= n:
                break
            index += 1

        index = 2

        for i in powers[2:]:
            for j in range(1, i):
                ones = j

                while index <= 2 ** (i - 1) + 2**j:
                    print("i", i, "j", j, "index", index, 2 ** (i - 1) + 2**j)
                    if index & 1:
                        out.append(ones + 1)
                    else:
                        out.append(ones)

                    index += 1
                    if index >= n:
                        return out

        return out


if __name__ == "__main__":
    s = Solution()
    print(s.countBits(8))
