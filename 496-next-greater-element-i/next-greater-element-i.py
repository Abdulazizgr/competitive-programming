class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_gre = defaultdict(lambda : -1)
        stack = []

        for num in nums2:
            while stack and stack[-1] < num:
                val = stack.pop()
                next_gre[val] = num
            stack.append(num)
        return [next_gre[num] for num in nums1]
