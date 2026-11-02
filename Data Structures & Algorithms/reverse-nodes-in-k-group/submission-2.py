# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, start, end) -> Optional[ListNode]:
        prev = end
        curr = start
        while curr != end:
            storeNext = curr.next
            curr.next = prev
            prev = curr
            curr = storeNext
        return prev

    def traverseK(self, node, k) -> Optional[ListNode]:
        while node and k > 0:
            node = node.next
            k -= 1
        return node

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy
        while True:
            kth = self.traverseK(groupPrev, k)
            if not kth:
                return dummy.next
            groupNext = kth.next
            groupPrevTemp = groupPrev.next
            groupPrev.next = self.reverseList(groupPrev.next, groupNext)
            groupPrev = groupPrevTemp  