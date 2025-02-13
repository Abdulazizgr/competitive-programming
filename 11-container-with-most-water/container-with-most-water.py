class Solution:
    def maxArea(self, height: List[int]) -> int:
        left  = 0
        right = len(height) -1
        max_area = 0
        while left < right :
            min_num = min(height[left],height[right])
            max_area = max(max_area,min_num * (right - left))
            
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return max_area