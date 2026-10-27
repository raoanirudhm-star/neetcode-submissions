# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        s = 0
        while curr:
            curr = curr.next
            s += 1
        curr = head
        if s - n - 1 >= 0:
            for i in range(s - n - 1):
                curr = curr.next
            curr.next = curr.next.next
            return head
        else:
            return head.next
        