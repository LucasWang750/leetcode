# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        
        visited = []
        h = head
        has_cycle = False
        
        while h != None:
            
            if h in visited:
                has_cycle = True
                break
            visited.append(h)
            
            h = h.next
            
        return has_cycle