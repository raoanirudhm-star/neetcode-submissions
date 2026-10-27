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
        prev = head
        ans = prev
        if s - n - 1 >= 0:
            for i in range(s - n - 1):
                prev = prev.next
            prev.next = prev.next.next
            return head
        else:
            return ans.next
        