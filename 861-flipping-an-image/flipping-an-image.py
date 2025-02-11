class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            row.reverse()
        for row in range(len(image)):
            for col in range(len(image)):
                if image[row][col] == 0:
                     image[row][col] = 1
                else:
                     image[row][col] = 0
        return image
