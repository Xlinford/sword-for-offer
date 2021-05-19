from typing import List
import ipdb


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mirrorTree1(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = root.right, root.left
            root.right = self.mirrorTree1(root.right)
            root.left = self.mirrorTree1(root.left)
        return root

    def mirrorTree(self, root: TreeNode) -> TreeNode:
        stack = root and [root]
        while stack:
            n = stack.pop()
            if n:
                n.left, n.right = n.right, n.left
                stack += n.right, n.left
        return root

    def isSymmetric(self, root: TreeNode) -> bool:
        def is_same(t1, t2):
            if t1 and t2:
                return t1.val == t2.val and is_same(t1.left, t2.right) and is_same(t1.right, t2.left)
            else:
                return t1 is t2

        if not root:
            return True
        return is_same(root.left, root.right)

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return (matrix and list(matrix.pop(0)) +
                self.spiralOrder(list(zip(*matrix))[::-1]))

    def pin_spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        n, m = len(matrix), len(matrix[0])
        list = []
        a, b, c, d = 0, 0, n - 1, m - 1
        while a <= c and b <= d:
            for i in range(b, d+1):
                list.append(matrix[a][i])
            for j in range(a+1, c+1):
                list.append(matrix[j][d])
            if a < c and b < d:
                for i in range(d-1, b, -1):
                    list.append(matrix[c][i])
                for j in range(c, a, -1):
                    list.append(matrix[j][b])
            a += 1
            b += 1
            c -= 1
            d -= 1
        return list

    def antispiralOrder(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return None
        reverse_ma = list(zip(*(matrix[::-1])))
        a = list(reverse_ma.pop(0))[::-1]
        return a + self.antispiralOrder(reverse_ma)
