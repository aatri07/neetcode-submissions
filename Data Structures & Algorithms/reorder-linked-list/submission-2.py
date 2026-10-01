# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next.next: return


        # Find middle of the list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None

        # Reverse second half
        prev = None
        curr = second
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        second = prev

        # Interleave
        first = head
        while second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next
        return

    
        