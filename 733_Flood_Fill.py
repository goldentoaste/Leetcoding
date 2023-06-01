from typing import List, Set, Dict


class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """

        if image[sr][sc] == color:
            return image

        original = image[sr][sc]
        image[sr][sc] = color
        if sr > 0 and image[sr - 1][sc] == original:
            self.floodFill(image, sr - 1, sc, color)

        if sr < len(image) - 1 and image[sr + 1][sc] == original:
            self.floodFill(image, sr + 1, sc, color)

        if sc > 0 and image[sr][sc - 1] == original:
            self.floodFill(image, sr, sc - 1, color)

        if sc < len(image[0]) - 1 and image[sr][sc + 1] == original:
            self.floodFill(image, sr, sc + 1, color)

        return image


if __name__ == "__main__":
    o = Solution()
    # image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

    # image = o.floodFill(image, 1, 1, 2)
    
    image = [[0,0,0],[0,0,0]]

    image = o.floodFill(image, 0,0,0)

    for i in image:
        o = ""
        for item in i:
            o += str(item)

        print(o)
