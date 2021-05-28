from typing import List


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp, a, b, c = [1] * n, 0, 0, 0
        for i in range(1, n):
            n2, n3, n5 = dp[a] * 2, dp[b] * 3, dp[c] * 5
            dp[i] = min(n2, n3, n5)
            if dp[i] == n2:
                a += 1
            if dp[i] == n3:
                b += 1
            if dp[i] == n5:
                c += 1
        return dp[-1]

    def firstUniqChar(self, s: str) -> str:
        dic = {}
        for i in s:
            dic[i] = not i in dic
        for key, v in dic.items():
            if v: return key
        return ' '

    def reversePairs(self, nums: List[int]) -> int:
        def reverse(l, r):
            if l >= r: return 0
            m = (l + r) // 2
            res = reverse(l, m) + reverse(m + 1, r)
            i, j = l, m + 1
            tem[l:r + 1] = nums[l:r + 1]
            for k in range(l, r + 1):
                if i == m + 1:
                    nums[k] = tem[j]
                    j += 1
                elif j == r + 1 or tem[i] <= tem[j]:
                    nums[k] = tem[i]
                    i += 1
                else:
                    nums[k] = tem[j]
                    j += 1
                    res += m - i + 1
            return res

        tem = [0] * len(nums)
        return reverse(0, len(nums) - 1)
