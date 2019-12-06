# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if(head):
            curr = head.next
            steady = head.next
            prev = head
            prev.next = None
            
            while(steady):
                steady = steady.next
                curr.next = prev
                prev = curr
                curr = steady
            
            return prev
