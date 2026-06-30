# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr = head

        carry = 0
        while l1 or l2: 
            v1 = 0
            v2 = 0
            if l1:
                v1 = l1.val
            if l2: 
                v2 = l2.val
            
            val = v1 + v2 + carry
            #since its in reverse
            #carry divided by 10 and quotient is mod 10
            carry = val // 10 
            val = val % 10

            curr.next = ListNode(val)
            curr = curr.next
            if l1: 
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry > 0: 
            curr.next = ListNode(carry)
            curr = curr.next    
        return head.next
        
