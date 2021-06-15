# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if preorder == []:
            return None
        value = preorder[0]
        root = TreeNode(value)
        cut = inorder.index(value)
        root.left = self.buildTree(preorder[1:cut + 1], inorder[:cut])
        root.right = self.buildTree(preorder[cut + 1:], inorder[cut + 1:])
        return root

class CQueue:

    def __init__(self):
        self.a=[]
        self.b=[]

    def appendTail(self, value: int) -> None:
        self.a.append(value)

    def deleteHead(self) -> int:
        if self.b:
            return self.b.pop()
        elif self.a:
            while self.a:
                self.b.append(self.a.pop())
            return self.b.pop()
        else:
            return -1