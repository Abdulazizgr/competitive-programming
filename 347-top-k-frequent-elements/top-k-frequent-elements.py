class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        ans = []
        arr = []
        for val in cnt:
            ans.append((cnt[val],val))
        ans.sort(reverse = True)
        for i in range(k):
            arr.append(ans[i][1])
        return arr
            
