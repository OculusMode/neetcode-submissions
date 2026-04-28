class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        h = {}
        for i in nums:
            if i in h:
                h[i]+=1
            else:
                h[i] = 0
        l = len(nums)//2
        for i, j in h.items():
            if j >= l:
                return i