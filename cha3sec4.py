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