"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        mymap = {}
        if head == None: 
            return None
        temp = Node(head.val) 
        tail = temp
        curr = head
        while curr: 
            mymap[curr] = tail
            curr = curr.next
            if(curr != None):
                tail.next = Node(curr.val)
        
            tail = tail.next

        tempy = head
        tempy2 = temp
        print(mymap)
        while tempy: 
            
            if tempy.random != None: 
                tempy2.random = mymap[tempy.random]
            else: 
                tempy2.random = None
            tempy = tempy.next
            tempy2 = tempy2.next
        
        return temp
