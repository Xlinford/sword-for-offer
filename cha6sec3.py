import collections
from typing import List
from main import TreeNode
import queue

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find(tar):
            i, j = 0, len(nums) - 1
            while i <= j:
                m = (i + j) // 2
                if nums[m] <= tar:
                    i = m + 1
                else:
                    j = m - 1
            return i

        return find(target) - find(target - 1)

    def missingNumber(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if m == nums[m]:
                i = m + 1
            else:
                j = m - 1
        return i

    def kthLargest(self, root: TreeNode, k: int) -> int:
        self.stack = root.val
        self.k = k

        def dfs(node):
            if not node: return
            dfs(node.right)
            if self.k == 0: return
            self.k -= 1
            if self.k == 0:
                self.stack = node.val
            dfs(node.left)

        dfs(root)
        return self.stack

    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def isBalanced(self, root: TreeNode) -> bool:
        def recur(root):
            if not root: return 0
            left = recur(root.left)
            if left == -1: return -1
            right = recur(root.right)
            if right == -1: return -1
            return max(left, right) + 1 if abs(right - left) <= 1 else -1

        return recur(root) != -1

    def singleNumbers(self, nums: List[int]) -> List[int]:
        a, b = nums[0], 1
        for i in nums[1:]:
            a ^= i
        x, y = 0, 0
        while a & b == 0:
            b <<= 1
        for i in nums:
            if i & b:
                x ^= i
            else:
                y ^= i
        return [x, y]

    def singleNumber(self, nums: List[int]) -> int:
        one, two = 0, 0
        for num in nums:
            one = one ^ num & ~two
            two = two ^ num & ~one
        return one

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pre, cur = 0, len(nums) - 1
        while pre <= cur:
            numsum = nums[pre] + nums[cur]
            if numsum == target:
                break
            elif numsum > target:
                cur -= 1
            else:
                pre += 1
        return [nums[pre], nums[cur]]

    def findContinuousSequence(self, target: int) -> List[List[int]]:
        i, j, s, res = 1, 2, 3, []
        while i < j:
            if s == target:
                res.append(list(range(i, j + 1)))
            if s >= target:
                s -= i
                i += 1
            else:
                j += 1
                s += j
        return res

    def reverseWords(self, s: str) -> str:
        s = s.strip()
        i = j = len(s) - 1
        res = []
        while i>=0:
            while i>=0 and s[i] != ' ':
                i -= 1
            res.append(s[i+1:j+1])
            while s[i] == ' ':
                i -= 1
            j = i
        return ' '.join(res)

    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[:n]

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque = collections.deque()
        res, n = [], len(nums)
        for i, j in zip(range(1 - k, n + 1 - k), range(n)):
            # 删除 deque 中对应的 nums[i-1]
            if i > 0 and deque[0] == nums[i - 1]:
                deque.popleft()
            # 保持 deque 递减
            while deque and deque[-1] < nums[j]:
                deque.pop()
            deque.append(nums[j])
            # 记录窗口最大值
            if i >= 0:
                res.append(deque[0])
        return res

class MaxQueue:

    def __init__(self):
        self.queue = queue.Queue()
        self.deque = collections.deque()

    def max_value(self) -> int:
        if not self.deque: return -1
        return self.deque[0]

    def push_back(self, value: int) -> None:
        self.queue.put(value)
        while self.deque and self.deque[-1] < value:
            self.deque.pop()
        self.deque.append(value)

    def pop_front(self) -> int:
        if self.queue.empty(): return -1
        val = self.queue.get()
        if val == self.deque[0]:
            self.deque.popleft()
        return val
