# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        fast = head.next
        slow = head
        #iterate to end and halfway point
        while fast and fast.next: 
            fast = fast.next.next
            slow = slow.next

        #disconnect second half and
        #set head and previous node 
        secondHalf = slow.next
        prev = None
        slow.next = None
        while secondHalf:
            #next = curr next
            #
            tmp = secondHalf.next
            secondHalf.next = prev
            prev = secondHalf 
            secondHalf = tmp

        #once it is reversed then merge 
        #prev is the new head
        curr = head

        while prev != None:
            temp = curr.next
            temp2 = prev.next
            curr.next = prev
            prev.next = temp
            curr = temp
            prev = temp2

        
      


            

        

