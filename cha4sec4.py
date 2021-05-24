from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class RandomNode:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def copyRandomList(self, head: 'RandomNode') -> 'RandomNode':
        dic = {None: None}
        n = m = head
        while n:
            dic[n] = RandomNode(n.val, None, None)
            n = n.next
        while m:
            dic[m].next = dic[m.next]
            dic[m].random = dic[m.random]
            m = m.next
        return dic[head]

    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def dfs(cur):
            if not cur: return None
            dfs(cur.left)
            if self.pre:
                self.pre.right, cur.left = cur, self.pre
            else:
                self.head = cur
            self.pre = cur
            dfs(cur.right)

        if not root: return None
        self.pre = None
        dfs(root)
        self.pre.right, self.head.left = self.head, self.pre
        return self.head

    def permutation(self, s: str) -> List[str]:
        ans = ['']
        for st in s:
            ans = [p[:i] + st + p[i:]
                   for p in ans for i in range((p + st).index(st) + 1)]
            print(ans)
        return sorted(ans) if s else []

class Codec:

    def serialize(self, root):
        if not root: return "[]"
        queue = root and [root]
        res = []
        while queue:
            node = queue.pop(0)
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("null")
        return '[' + ','.join(res) + ']'

    def deserialize(self, data):
        if data == "[]": return
        vals, i = data[1:-1].split(','), 1
        root = TreeNode(int(vals[0]))
        queue = [root]
        while queue:
            node = queue.pop(0)
            if vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            if vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
        return root



if __name__ == "__main__":
    a = [1, 2, 3, None, None, 4, 5]
    stack = []
    for i in a:
        node = TreeNode(i)
        stack.append(node)
    node = stack[0]
    node.left = stack[1]
    node.right = stack[2]
    node.right.left = stack[5]
    node.right.right = stack[6]
    code =Codec()
    solu = Solution()
    s = "abc"
    print(solu.permutation(s))

