class Solution:
    def trap(self, height: List[int]) -> int:
        # for a unit height to have water
        # it should have some pillar on right, and some on left
        # both bigger than it
        # i.e. for 5th(starting from 0) height, 3 and 7 have 3 height
        # so water is min(3, 3) - height[5] = 3 - 0 = 3
        # for 4th, min(3, 3) - 1 = 2
        l = len(height)
        a = 0
        right_max = 0
        left_max = 0
        rights = [0] * l
        lefts = [0] * l
        for idx, h in enumerate(height):
            lefts[idx] = left_max
            left_max = max(left_max, h)
        for idx, h in enumerate(height[::-1]):
            rights[l - 1 - idx] = right_max
            right_max = max(right_max, h)
        print(lefts, rights)
        for idx in range(l):
            a += max(0,(min(rights[idx], lefts[idx]) - height[idx]))
        return a
        