# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head
        i = 0
        while (fast != None and fast.next != None):
            fast = fast.next.next
            slow = slow.next
        
        second = slow.next
        slow.next = None
        
        prev = None
        curr = second
        while (curr != None):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        first = head
        second = prev
        while (second != None):
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2

        
            


            


        