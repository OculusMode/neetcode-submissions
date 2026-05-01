class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = len(nums)
        s = 0
        e = l - 1
        while s <= e:
            m = s + (e - s)//2
            mid = nums[m]
            # print(s, e, mid)
            if mid == target:
                return m
            first = nums[s]
            last = nums[e]
            left_messed = mid < first
            if left_messed:
                # if right is simple, if element is between mid and end, its on right side, else left
                if mid < target and last >= target:
                    s = m + 1
                else:
                    e = m - 1
            else:
                # same logic for left side
                if first <= target and mid > target:
                    e = m - 1
                else:
                    s = m + 1

        return -1