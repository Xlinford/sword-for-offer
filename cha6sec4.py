import collections
from typing import List
from main import TreeNode

class Solution:
    def __init__(self):
        self.a = 123
    def dicesProbability(self, n: int) -> List[float]:
        dp = [1/6]*6
        for i in range(2, n+1):
            tmp = [0]*(5*i+1)
            for j in range(len(dp)):
                for k in range(6):
                    tmp[j+k] += dp[j]/6
            dp = tmp
        return dp

    def isStraight(self, nums: List[int]) -> bool:
        def numsort(l, r):
            i, j = l, r
            while i < j:
                while i < j and nums[i] < nums[l]: i += 1
                while i < j and nums[j] > nums[l]: j -= 1
                if nums[i] != nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                else:
                    j -= 1
            nums[i], nums[l] = nums[l], nums[i]
            if l < r:
                numsort(l, i - 1)
                numsort(i + 1, r)

        numsort(0, len(nums) - 1)
        joker = 0
        for i in range(4):
            if nums[i] == 0: joker += 1
            elif nums[i] == nums[i+1]: return False
        return nums[-1] - nums[joker] < 5

    def lastRemaining(self, n: int, m: int) -> int:
        x = 0
        for i in range(2, n+1):
            x = (m + x) % i
        return x

    def maxProfit(self, prices: List[int]) -> int:
        cost, profit = float('+inf'), 0
        for i in prices:
            cost = min(cost, i)
            profit = max(profit, cost-i)
        return profit

sol = Solution()
print(sol.isStraight([0,0,3,2,6]))