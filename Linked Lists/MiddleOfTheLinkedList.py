# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
#    def length(self):

 #       return length
#    def __init__(self):
 #       self.head=ListNode(self)
    
    def middleNode(self, head: ListNode) -> ListNode:
        llist = head
        length = 0
        cur_node=llist
        while cur_node:
            length = length +1
            cur_node = cur_node.next
        print(length)    
    
        ans= ((length//2)) 
       # if length == 1:
       #     return llist
       # elif length ==2:
       #     return llist.next
        result = llist
        del_node = result
        index=0
        while del_node:
            if (ans==index):
                result=del_node
                
                return result
            del_node = del_node.next
            index = index + 1
       
        
        

        
        
