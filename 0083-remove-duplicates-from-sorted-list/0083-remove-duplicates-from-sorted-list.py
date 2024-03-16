# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        unique = head
        duplicate = False
        while unique != None:
            second = unique.next
            
            while second != None and unique.val == second.val:
                duplicate = True
                second = second.next
            if duplicate:
                unique.next = second
            unique = unique.next
            
        
        return head