# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        dummy = ans
        remainder = 0
        while l1 and l2:
            ans.next = ListNode((l1.val + l2.val + remainder) % 10)
            remainder = (l1.val + l2.val + remainder) // 10
            ans = ans.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            ans.next = ListNode((l1.val + remainder) % 10)
            remainder = (l1.val + remainder) // 10
            ans = ans.next
            l1 = l1.next
        while l2:
            ans.next = ListNode((l2.val + remainder) % 10)
            remainder = (l2.val + remainder) // 10
            ans = ans.next
            l2 = l2.next
        if remainder != 0:
            ans.next = ListNode(remainder)
        return dummy.next
        
        


        