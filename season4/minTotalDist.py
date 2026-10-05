from typing import List, Set, Dict, Optional
null = None


def getMinTotalDistance(dist_centers: List[int])->int:
    '''
    https://aonecode.com/amazon-online-assessment/Get-Minimum-Total-Distance

    Divide the given numbers into 2 groups, such that each group's distance to average is minimized.
    return sum of distance to both group's centers.
    '''

    if not dist_centers:
        return -1

    if len(dist_centers) <3:
        return 0
    dist_centers.sort()
    A = [dist_centers[0]]
    B = [dist_centers[-1]]

    aAvg = A[0]
    bAvg = B[0]


    for d in dist_centers[1: -1]:
        diffA = abs(aAvg - d)
        diffB = abs(bAvg - d)

        if diffA < diffB:
            aAvg = ((aAvg * len(A) + d) / (len(A) + 1))
            A.append(d)
        else:
            bAvg = ((bAvg * len(B) + d) / (len(B) + 1))
            B.append(d)

    total = 0
    for a in A:
        total += abs(aAvg - a)
    for b in B:
        total += abs(bAvg - b)

    return int(total)





if __name__ == "__main__":

    print(getMinTotalDistance( [4, 1, 5, 99, 100])) # 5

    print(getMinTotalDistance( [1, 2, 3]))