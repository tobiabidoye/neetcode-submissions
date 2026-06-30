# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        count = 0
        while fast != None: 
            fast = fast.next
            count += 1

        if count == n: 
            return head.next
        print(count)
        slow = head
        count2 = 1
        while count2 < (count - n): 
            slow = slow.next
            print(count2)
            count2 += 1
        
        slow.next = slow.next.next
        return head