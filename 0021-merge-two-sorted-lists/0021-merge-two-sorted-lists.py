# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        temp1 = list1
        temp2 = list2
        res = ListNode()
        # result = temp1 if list1.val <= list2.val else temp2
        result = res
        while temp1 and temp2:
            if temp1.val < temp2.val:
                result.next = temp1
                temp1 = temp1.next
            else:
                result.next = temp2
                temp2 = temp2.next
            result = result.next
        while temp1:
            result.next = temp1
            temp1 = temp1.next
            result = result.next
        while temp2:
            result.next = temp2
            temp2 = temp2.next
            result = result.next
        return res.next