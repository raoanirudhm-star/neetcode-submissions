# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def merge(self, a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        while a and b:
            if a.val < b.val:
                curr.next = a
                a = a.next
            else:
                curr.next = b
                b = b.next
            curr = curr.next
        if a:
            curr.next = a
        else:
            curr.next = b
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None 
        while len(lists) > 1:
            mergedList = []
            for i in range(0, len(lists), 2):
                first = lists[i]
                second = lists[i+1] if i+1 < len(lists) else None
                if second:
                    mergedList.append(self.merge(first, second))
                else:
                    mergedList.append(first)
            lists = mergedList
        return lists[0]


        