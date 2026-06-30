# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        nexty = None
        prev = None
        
        while(head != None):
            nexty = head.next
            head.next = prev
            prev = head
            head = nexty

        #return list head
        return prev
        
        

        