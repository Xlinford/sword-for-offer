from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dic = {None: None}
        n = m = head
        while n:
            dic[n] = Node(n.val, None, None)
            n = n.next
        while m:
            dic[m].next = dic[m.next]
            dic[m].random = dic[m.random]
            m = m.next
        return dic[head]

