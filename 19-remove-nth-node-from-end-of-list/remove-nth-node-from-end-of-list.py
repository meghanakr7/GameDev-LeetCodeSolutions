# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        sec = dummy
        i = 0
        while i < n + 1:
            first = first.next
            i += 1
        while first!=None:
            first = first.next
            sec = sec.next
        sec.next = sec.next.next
        return dummy.next