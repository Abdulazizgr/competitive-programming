class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        ans = []
        for idx in range(1,len(height)):
            if height[idx-1] > threshold:
                ans.append(idx)
        return ans