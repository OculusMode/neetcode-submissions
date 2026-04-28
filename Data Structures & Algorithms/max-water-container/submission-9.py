class Solution:
    def maxArea(self, heights: List[int]) -> int:
        m = 0
        f, l = 0, len(heights) - 1
        while f < l:
            f_ = heights[f]
            l_ = heights[l]
            area = min(f_, l_) * (l - f)
            print(area, f_, l_)
            m = max(m, area)
            print(m)
            if f_ < l_:
                f+=1
            else:
                l-=1
        return m
