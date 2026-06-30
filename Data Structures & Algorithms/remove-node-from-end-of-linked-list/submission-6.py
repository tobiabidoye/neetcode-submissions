# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head1 = head
        tail = head1
        #count number of nodes
        count = 0
        while tail: 
            count += 1
            tail = tail.next

        #now that we have the count 
        count2 = 0
        curr = head1
        prev = None
        while (count - count2) != n:
            prev = head1
            head1 = head1.next
            count2 += 1
        
        print(head1.val)
        if prev == None: 
            return head1.next
        else: 
            prev.next = head1.next
            return curr

        return curr