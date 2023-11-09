# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = head
        firstcopy = first
        f = 0
        s = 0
        def gcd(a, b):
            if a < b:
                s = a
                l = b
            else:
                s = b
                l = a
            while s:
                if a%s == 0 and b%s == 0:
                    return s
                s -= 1
        while head:
            f = head.val
            if head and head.next:
                temp = head.next
                s = head.next.val
                v = gcd(f, s)
                newNode = ListNode(v)
                head.next = newNode
                head.next.next = temp
                head = head.next.next
            else:
                break
        return first
         

        