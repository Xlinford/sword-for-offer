from heapq import *
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            if count == 0: x = i
            count += 1 if x == i else -1
        return x

    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k >= len(arr): return arr

        def sortk(l, r):
            i, j = l, r
            while i < j:
                while i < j and arr[j] > arr[l]: j -= 1
                while i < j and arr[i] < arr[l]: i += 1
                arr[i], arr[j] = arr[j], arr[i]
            arr[i], arr[l] = arr[l], arr[i]
            if i > k: return sortk(l, i - 1)
            if i < k: return sortk(i + 1, r)
            return arr[:k]

        return sortk(0, len(arr) - 1)

    class MedianFinder:

        def __init__(self):
            """
            initialize your data structure here.
            """
            self.A = []
            self.B = []

        def addNum(self, num: int) -> None:
            if len(self.A) != len(self.B):
                heappush(self.A, num)
                heappush(self.B, -heappop(self.A))
            else:
                heappush(self.B, -num)
                heappush(self.A, -heappop(self.B))

        def findMedian(self) -> float:
            return self.A[0] if len(self.A) != len(self.B) else (self.A[0] - self.B[0]) / 2

    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        return max(nums)

    def maxSubArray1(self, nums: List[int]) -> int:
        max = nums[0]
        dp = nums[0]
        for i in range(1, len(nums)):
            if dp > 0:
                dp += nums[i]
            else:
                dp = nums[i]
            if dp > max:
                max = dp
        return max

    def countDigitOne(self, n: int) -> int:
        digit, res = 1, 0
        high, cur, low = n // 10, n % 10, 0
        while high != 0 or cur != 0:
            if cur == 0:
                res += high * digit
            elif cur == 1:
                res += high * digit + low + 1
            else:
                res += (high + 1) * digit
            low += cur * digit
            cur = high % 10
            high //= 10
            digit *= 10
        return res

    def findNthDigit(self, n: int) -> int:
        digit, start, count = 1, 1, 9
        while n > count:
            n -= count
            start = 10 ** digit
            digit += 1
            count = start * 9 * digit
        num = start + (n - 1) // digit
        return int(str(num)[(n - 1) % digit])

    def minNumber(self, nums: List[int]) -> str:
        def quick_sort(l, m):
            if l >= m: return
            a, b = l, m
            while a < b:
                while strnums[l] + strnums[b] < strnums[b] + strnums[l] and a < b: b -= 1
                while strnums[l] + strnums[a] > strnums[a] + strnums[l] and a < b: a += 1
                strnums[a], strnums[b] = strnums[b], strnums[a]
            strnums[a], strnums[l] = strnums[l], strnums[a]
            quick_sort(l, a - 1)
            quick_sort(a + 1, m)

        strnums = [str(i) for i in nums]
        quick_sort(0, len(strnums) - 1)
        return ''.join(strnums)

    def translateNum(self, num: int) -> int:
        ns = str(num)
        a, b = 1, 1
        for i in range(2, len(ns) + 1):
            slice = ns[i - 2:i]
            c = a + b if 10 <= int(slice) <= 25 else b
            a = b
            b = c
        return b

    def maxValue(self, grid: List[List[int]]) -> int:
