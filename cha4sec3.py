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

    def levelOrderRow(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        nodelist = []
        stack = [root]
        while stack:
            nodelist.append([i.val for i in stack])
            stack = [j for i in stack for j in (i.left, i.right) if j]
        return nodelist

    def levelOrderRowZhi(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        nodelist = []
        stack = [root]
        flag = -1
        while stack:
            nodelist.append([i.val for i in stack])
            if flag == -1:
                stack = [j for i in stack for j in (i.right, i.left) if j]
            else:
                stack = [j for i in stack[::-1] for j in (i.left, i.right) if j]
            flag *= -1
        return nodelist

    def verifyPostorder(self, postorder: List[int]) -> bool:
        def method(poslist: List[int], start: int, end: int):
            if start >= end:
                return True
            mid = start
            while poslist[mid] < poslist[end]:
                mid += 1
            for i in range(mid, end+1):
                if poslist[i] < poslist[end]:
                    return False

            return method(poslist, start, mid-1) and method(poslist, mid, end-1)
        return method(postorder, 0, len(postorder)-1)

    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        stack = root and [root, root.val, ]
        pathlist = [[]]
        while stack:
            i = 0
            for node in stack:
                pathlist[i].append(node.val)
                listsum = sum(pathlist[i])
                if listsum > target:
                    pathlist.pop(i)
                elif listsum == target:
                    continue
                else:
                    if not node.left:
                        stack.pop(i)
                        stack.append(node.left)

                    pathlist.append(pathlist[-1])
                    stack.append(node.right)
                i += 1
        return pathlist