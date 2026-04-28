class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        l = len(nums)
        out = [1]*l
        for idx, num in enumerate(nums):
            out[idx] *= pre
            pre *= num
        post = 1
        for idx, num in enumerate(nums[::-1]):
            out[l-idx-1] *= post
            post *= num
        return out