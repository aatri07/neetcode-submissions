# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node_set = set()
        temp = head
        while (temp):
            size = len(node_set)
            if (temp in node_set):
                return True
            else:
                node_set.add(temp)
            temp = temp.next
        
        return False
        