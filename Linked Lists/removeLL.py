# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        #if the list is an empty list, return nothing
        if head == None:
            return
        
        #if head.next == None and head.val == val:
        #    return
        
        if head:
            curr = head 
            prev = head
            ans = prev
            
            while(curr and curr.val==val):
                curr = curr.next
                prev = prev.next
                ans = prev
                
            #if list is empty, return nothing
            if curr == None:
                return 
            
            curr = curr.next
            
            while curr:
                if curr == None:
                    return ans
                
                if curr.val==val:
                    prev.next = curr.next
                    curr = curr.next
                    
                    if curr == None:
                        return ans
                
                if curr.val!=val:
                    curr = curr.next
                    prev = prev.next
                    
                
            return ans
            
            
            
   
            
       