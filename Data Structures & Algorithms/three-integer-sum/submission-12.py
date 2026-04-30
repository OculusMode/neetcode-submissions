class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        l = len(nums)
        nums.sort()
        for idx, i in enumerate(nums):
            jidx = idx + 1
            kidx = l - 1
            while kidx > jidx:
                j = nums[jidx]
                k = nums[kidx]
                if j + k == -1*i:
                    res.add(tuple(sorted([i, j, k])))
                    kidx -= 1
                elif j + k > -1*i:
                    kidx -= 1
                else:
                    jidx += 1
        return [list(i) for i in res]
