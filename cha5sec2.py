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
            if i > k: return sortk(l, i-1)
            if i < k: return sortk(i+1, r)
            return arr[:k]
        return sortk(0, len(arr)-1)

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
            return self.A[0] if len(self.A) != len(self.B) else (self.A[0]-self.B[0])/2

    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)
    def maxSubArray1(self, nums: List[int]) -> int:
        max = nums[0]
        dp = nums[0]
        for i in range(1, len(nums)):
            if dp > 0:
                dp += nums[i]
            else: dp = nums[i]
            if dp > max:
                max = dp
        return max

    def countDigitOne(self, n: int) -> int:
        digit, res = 1, 0
        high, cur, low = n//10, n%10, 0
        while high!=0 or cur!=0:
            if cur==0:res +=
