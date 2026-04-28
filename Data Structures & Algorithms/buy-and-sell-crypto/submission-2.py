class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_, max_ = 101, 0
        profit = 0
        for i in prices:
            # when new small value comes, we update max as well hoping for better profit
            if min_ > i:
                min_ = i
                max_ = i
            elif max_ < i:
                max_ = i
                profit = max(profit, max_-min_)
        return profit
            