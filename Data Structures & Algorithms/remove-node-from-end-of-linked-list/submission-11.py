# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        totalNodes = 0
        temp = head
        while (temp != None):
            totalNodes += 1
            temp = temp.next
        
        idx = 0
        nodeRemoveIdx = totalNodes - n
        temp = head
        while (temp != None):
            if (idx == nodeRemoveIdx - 1):
                prev = temp
                remove = temp.next
                prev.next = remove.next
                remove.next = None
                break
            if (idx == nodeRemoveIdx):
                head = head.next
                break
            idx += 1
            temp = temp.next
        
        return head
        