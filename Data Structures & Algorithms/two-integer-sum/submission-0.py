class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in hash_map:
                if hash_map[diff] == idx:
                    continue
                return sorted([hash_map[diff], idx])
            else:
                hash_map[num] = idx