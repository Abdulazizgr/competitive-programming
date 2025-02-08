class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows, cols = len(img), len(img[0])
        smoothed_img = [[0] * cols for _ in range(rows)] 

        def is_valid(row, col):
            return 0 <= row < rows and 0 <= col < cols  

        for row in range(rows):
            for col in range(cols):
                neighbors = [
                    (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1),
                    (row - 1, col - 1), (row + 1, col + 1), (row - 1, col + 1), (row + 1, col - 1)
                ]
                pixel_sum = img[row][col]
                pixel_count = 1

                for r, c in neighbors:
                    if is_valid(r, c):
                        pixel_sum += img[r][c]
                        pixel_count += 1

                smoothed_img[row][col] = pixel_sum // pixel_count  

        return smoothed_img  
