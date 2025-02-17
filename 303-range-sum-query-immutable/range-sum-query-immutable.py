class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.pre = [0] * (len(nums) + 1)  

        for i in range(len(nums)):
            self.pre[i + 1] = self.pre[i] + nums[i]  

    def sumRange(self, left: int, right: int) -> int:
        return self.pre[right + 1] - self.pre[left]  