class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        h = {}
        l = len(nums)//2
        for i in nums:
            if i in h:
                h[i]+=1
                if h[i] >= l:
                    return i
            else:
                h[i] = 0
        for i, j in h.items():
            if j >= l:
                return i