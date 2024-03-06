# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        fast = head.next
        slow = head
        if head and head.next is None:
            return False
        while fast != slow and slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if(fast is not None and fast == slow):
            return True
        return False        