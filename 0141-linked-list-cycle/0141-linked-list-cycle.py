# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        
        visited = set()
        h = head
        
        while h != None:
            
            if h in visited:
                return True
            visited.add(h)
            
            h = h.next
        
        return False