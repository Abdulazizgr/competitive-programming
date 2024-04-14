class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        ans = []
        for i in range(len(image)):
            num = image[i]
            num = num[::-1]
            num = [0 if i == 1 else 1 for i in num]
            ans.append(num)
        return ans