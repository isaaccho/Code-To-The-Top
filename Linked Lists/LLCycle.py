# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        fast = curr = head
        if(curr)==None:
            return False
        if(curr.next)==None:
            return False
        while curr:
            curr = curr.next
            fast = fast.next
            if(fast)==None:
                return False
            fast = fast.next
            if(fast)==None:
                return False
            if(curr.val == fast.val):
                return True
            
        return False