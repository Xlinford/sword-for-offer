from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = []

    def push(self, x: int) -> None:
        cur_min = self.min()
        if cur_min > x:
            cur_min = x
        self._stack.append((x, cur_min))

    def pop(self) -> None:
        self._stack.pop()

    def top(self) -> int:
        if not self._stack:
            return None
        else:
            return self._stack[-1][0]

    def min(self) -> int:
        if self._stack:
            return self._stack[-1][1]
        else:
            return float('inf')


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        j = 0
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        return j == len(popped)

    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        nodelist = []
        stack = [root]
        while stack:
            node = stack.pop(0)
            nodelist.append(node.val)
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)

        return nodelist
