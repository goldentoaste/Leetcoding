from typing import List, Set, Dict, Optional

null = None

# https://aonecode.com/interview-questions/Maximum-Greyness


def maxAcutance(image):
    """
    for each element, calc (# of 1 for this row + col) - (#0s at this row/col)
    """

    rows = len(image)
    cols = len(image[0])

    rowOnesCount = [0] * rows
    colOnesCount = [0] * cols

    acutance = float('-inf')

    for r, row in enumerate(image):
        for c, element in enumerate(row):
            if element == "1":
                rowOnesCount[r] += 1
                colOnesCount[c] += 1

    for i in range(rows):
        for j in range(cols):

            acutance = max(
                acutance,
                (rowOnesCount[i] + colOnesCount[j])
                - ((rows - rowOnesCount[i]) + cols - colOnesCount[j]),
            )

    return acutance


if __name__ == "__main__":
    print(maxAcutance(["101", "001", "110"]))
