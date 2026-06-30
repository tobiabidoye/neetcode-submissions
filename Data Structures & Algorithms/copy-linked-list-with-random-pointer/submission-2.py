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
        if not head: 
            return None 
        newHead = Node(head.val)
        mymap = {}
        tail = newHead
        curr = head.next
        mymap[head] = newHead 
        while curr != None: 
            newNode = Node(curr.val)
            tail.next = newNode
            tail = newNode
            mymap[curr] = tail
            curr = curr.next
            
        temp = head
        temp2 = newHead
        while temp: 
            temprand = temp.random
            if temp.random: 
                temp2.random = mymap[temp.random]
            else:
                temp2.random = None
            temp = temp.next
            temp2 = temp2.next

        return newHead
            
      



