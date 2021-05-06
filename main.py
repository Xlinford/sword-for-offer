def printListFromTailToHead(self, listNode):
    stack, h = [], listNode
    while h:
        stack.append(h.val)
        h = h.next
    return stack[::-1]

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 重建二叉树
def buildTree(preorder, inorder):
    if preorder == []:
        return None
    root_val = preorder[0]
    root = TreeNode(root_val)
    cut = inorder.index(root_val)
    root.left = buildTree(preorder[1:cut+1], inorder[:cut])
    root.right = buildTree(preorder[cut+1:], inorder[cut+1:])
    return root

# 二叉树的下一个节点
def GetNext(self, pNode):
    # write code here
    if not pNode:
        return None
    # 有右子树，右子树中最左节点
    if pNode.right:
        pre = pNode.right
        while pre.left:
            pre = pre.left
        return pre
    # 没有右子树，找父节点，或父节点的上一节点
    while pNode.next:
        parent = pNode.next
        if parent.left == pNode:
            return parent
        pNode = parent
    return None

# 两个栈实现队列
class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self) -> int:
        return self.s1.pop()

    def peek(self) -> int:
        return self.s1[-1]

    def empty(self) -> bool:
        return self.s1 == []

class Solution:
    def __init__(self):
        self.s1, self.s2=[],[]

    def push(self, node):
        # write code here
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s2.append(node)
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self):
        return self.s1.pop()
