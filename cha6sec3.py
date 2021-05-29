from typing import List
from main import TreeNode


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

