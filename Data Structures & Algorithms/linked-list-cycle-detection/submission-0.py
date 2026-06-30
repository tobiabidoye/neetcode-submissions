# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        mymap = {}
        while head != None: 
            mymap[id(head)] = "visited"
            if id(head.next) in mymap: 
                return True 
            head = head.next


        
        return False 

        