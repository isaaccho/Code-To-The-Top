# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
#    def length(self):

 #       return length
   # def __init__(self):
    #    self.head=ListNode(null)
    
    def middleNode(self, head: ListNode) -> ListNode:
        length = 0
        cur_node=self.ListNode
        while cur_node.next!=None:
            length = length +1
            cur_node = cur_node.next
            
    
        ans= (length/2) 
        cur_node = self.ListNode
        del_node = cur_node
        index=0
        while del_node.next !=None:
            if (ans==index):
                cur_node.next=del_node
            del_node = del_node.next
        return cur_node
        
        
        
