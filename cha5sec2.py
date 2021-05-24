from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            if count == 0: x = i
            count += 1 if x == i else -1
        return x

    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
