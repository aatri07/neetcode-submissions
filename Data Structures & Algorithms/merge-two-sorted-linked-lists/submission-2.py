# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        if (curr1 == None):
            return curr2
        elif (curr2 == None):
            return curr1
        res = None
        if (curr2.val <= curr1.val):
            res = curr2
            curr2 = curr2.next
        else:
            res = curr1
            curr1 = curr1.next
        og = res
        while (curr1 or curr2):
            if (curr1 == None):
                res.next = curr2
                curr2 = curr2.next
            elif (curr2 == None):
                res.next = curr1
                curr1 = curr1.next
            else: 
                if (curr1.val <= curr2.val):
                    res.next = curr1
                    curr1 = curr1.next
                else:
                    res.next = curr2
                    curr2 = curr2.next
            res = res.next
        
        return og
