class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        fastnode = slownode = head
        for _ in range(k - 1):
            if not fastnode:
                return fastnode.next
            fastnode = fastnode.next
        while fastnode:
            fastnode, slownode = fastnode.next, slownode.next
        return slownode

    def detectCycle(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                break
        else:
            return None
        while fast is not head:
            fast, head = fast.next, head.next
        return head

    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            head.next, prev, head = prev, head, head.next
        return prev

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l = head = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                l.next, l1 = l1, l1.next
            else:
                l.next, l2 = l2, l2.next
            l = l.next
        l.next = l1 or l2
        return head.next

    def mergeTwoLists1(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 or l2
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists1(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists1(l1, l2.next)
            return l2

    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def is_same(t1, t2):
            if not t2:
                return True
            elif not t1:
                return False
            else:
                return t1.val == t2.val and is_same(t1.left, t2.left) and is_same(t1.right, t2.right)
        if not A or not B:
            return False
        stack = A and [A]
        while stack:
            node = stack.pop()
            if node:
                if is_same(node, B):
                    return True
                stack.append(node.right)
                stack.append(node.left)
        return False




if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    solu = Solution
    rev_a = solu.reverseList(solu, a)
