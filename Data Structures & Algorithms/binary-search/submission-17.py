class Solution:
    def search(self, nums: List[int], target: int) -> int:
        e = len(nums) - 1
        s = 0
        return self.search_(nums, s, e, target)

    def search_(self, nums, start, end, target):
        l = end - start + 1
        mid = start + (l // 2)
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        if end == mid:
            return -1
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            return self.search_(nums, start, mid, target)
        else:
            if mid == start:
                mid += 1
            return self.search_(nums, mid, end, target)
