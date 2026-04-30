class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        j = {}
        for i in nums:
            j[i] = j.get(i, 0) + 1
        freq = [[] for _ in range(len(nums)+1)]
        for i, c in j.items():
            freq[c].append(i)
        res = []
        for i in range(len(nums), 0, -1):
            f = freq[i]
            if f:
                res.extend(f)
            if len(res) == k:
                return res
        return res