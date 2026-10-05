from itertools import chain
from typing import List, Set, Dict, Optional

null = None


def getSequence(dna: List[List[str]]) -> List[bool]:
    """
    given a list of pairs of strings, check if the 2 strings can be made equal
    if any number of a single char is removed from either/both strings
    they can be made equal.

    So basically get histogram of both strings, each difference is a modification
    can only be done iff only 1 modification is needed from each string
    """

    def getCount(s):
        out = [0] * 26
        for c in s:
            out[ord(c) - 97] += 1

        return out

    def canMod(s1: List[int], s2: List[int]):
        mod = False
        ineq = 0
        for idx, (c1, c2) in enumerate(zip(s1, s2)):
            if c1 != c2:
                ineq += 1
                if c1 > c2 and not mod:
                    mod = True
                    s1[idx] = c2
                    ineq -= 1
        return ineq == 0

    out = []
    for pair in dna:
        s1, s2 = pair

        his1 = getCount(s1)
        his2 = getCount(s2)

        m1 = canMod(his1, his2)
        m2 = canMod(his2, his1)

        out.append( m2)

    return out


if __name__ == "__main__":
    dna = [["abcee", "acdeedb"], ["sljffsajej", "sljsje"]]
    print(getSequence(dna))


    dna=[['noodle', 'needle']]
    print(getSequence(dna))
