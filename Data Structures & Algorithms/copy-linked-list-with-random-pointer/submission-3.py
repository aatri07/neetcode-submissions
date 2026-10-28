"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        og_to_copy = {None : None}
        temp = head
        while temp:
            og_to_copy[temp] = Node(temp.val, None, None)
            temp = temp.next
        temp = head
        while temp:
            copy = og_to_copy[temp]
            copy.next = og_to_copy[temp.next]
            copy.random = og_to_copy[temp.random]
            temp = temp.next
        
        return og_to_copy[head]
        

        