# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if(head):
            steady = head.next
            current = head.next
            final = head
            final.next = None
        
       
       # current = current.next

        #print(current)
        #while(current.next!=None):   
        # current = current.next
            while(steady):
                steady = steady.next
                current.next = final
                #steady = steady.next
                final = current
                current = steady
        
        
            return final
        