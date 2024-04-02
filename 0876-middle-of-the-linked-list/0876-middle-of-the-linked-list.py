# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        front = head
        middle = head
        count = 0
        
        while not front is None:
            if count == 1:
                middle = middle.next
                count = 0
            else:
                count += 1
            front = front.next
        
        return middle