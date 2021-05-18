class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        fastnode = slownode = head
        for _ in range(k-1):
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
            print(prev.val)
        return prev

if  __name__ == '__main__':
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