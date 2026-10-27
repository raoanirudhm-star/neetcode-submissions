# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        n = 0
        curr = head
        while curr:
            curr = curr.next
            n += 1
        mid = n // 2
        left = head
        for i in range(mid - 1):
            left = left.next
        right = left.next
        left.next = None
        prev = None
        while right:
            nxt = right.next
            right.next = prev
            prev = right
            right = nxt
        
        left = head
        right = prev
        while left and right:
            left_next = left.next
            right_next = right.next
            left.next = right
            right.next = left_next if left_next else right_next
            left = left_next
            right = right_next


        