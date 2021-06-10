import collections
from typing import List
from main import TreeNode


class Solution:
    def __init__(self):
        self.a = 0

    def sumNums(self, n: int) -> int:
        n > 1 and self.sumNums(n - 1)
        self.a += n
        return self.a

    def add(self, a: int, b: int) -> int:
        x = 0xffffffff
        a, b = a & x, b & x
        while b != 0:
            a, b = (a ^ b), (a & b) << 1 & x
        return a if a <= 0x7fffffff else ~(a ^ x)

    def constructArr(self, a: List[int]) -> List[int]:
        b, tmp = [1]*len(a), 1
        for i in range(1,len(a)):
            b[i] = b[i-1]*a[i-1]
        for j in range(len(a)-2, -1, -1):
            tmp *= a[j+1]
            b[j] *= tmp
        return b

    def strToInt(self, str: str) -> int:
        str = str.strip()
        if not str: return 0
        res, i, sign = 0, 1, 1
        int_max, int_min, bndry = 2 ** 31 - 1, -2 ** 31, 2**31//10
        if str[0] == '-': sign = -1
        elif str[0] != '+': i = 0
        for c in str:
            if not '0'<=c<'9': return res
            if res>bndry or res==bndry and c>'7': return int_max if sign==1 else int_min
            res = res*10+ord(c)
        return res

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val: p, q = q, p
        while root:
            if root.val>q.val:
                root = root.left
            elif root.val<p.val:
                root = root.right
            else:
                break
        return root

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left: return right
        if not right: return left
        return root
