class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 1 2 3 4 5 6
        # 5 6 1 2 3 4
        # 3 4 5 6 1 2=> tempered, hence min is <= 2
        # 5 6 1 2 3 4 => min <= 4, 1 <= 4, yes, so check left more
        # 3 4 5 6 1 2=> min is <= 2, 5 <= 2, no, so check right
        l = len(nums)
        if nums[0] <= nums[-1]:
            return nums[0] # sorted arr
        leastMin = nums[-1]
        s = 0
        e = l - 1
        while s <= e:
            mid = s + (e - s)//2
            if nums[mid] < leastMin:
                leastMin = nums[mid]
                e = mid - 1
            if nums[mid] > leastMin:
                s = mid + 1
            else:
                e = mid - 1
        return leastMin
