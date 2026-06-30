# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #get to middle point
        slow = head
        fast = head.next

        while fast: 
            slow = slow.next
            temp = fast.next 
            if temp == None:
                break
            fast = temp.next
        
        #reverse second half
        second = slow.next
        slow.next = None
        prev = None

        while second:
            nexty = second.next
            second.next = prev
            prev = second
            second = nexty
        
        #after reversing merge

        #prev is new head of second half

        while prev:
            temp = head.next
            temp2 = prev.next  
            
            head.next = prev
            prev.next = temp

            prev = temp2
            head = temp
        
