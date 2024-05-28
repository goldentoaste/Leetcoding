class SolutionOld(object):
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


class Solution(object):
    def countBits(self, n: int):
        mem = [0] * (n + 1)
        for i in reversed(range(1, n + 1)):
            if mem[i] != 0:
                continue
            indices = []
            while i > 0:
                if mem[i] != 0:
                    for index in indices:
                        mem[index] += mem[i]
                    break   
                indices.append(i)
                if i & 1:
                    for index in indices:
                        mem[index] += 1
                i = i//2


        return mem


if __name__ == "__main__":
    s = Solution()
    print(s.countBits(8))
