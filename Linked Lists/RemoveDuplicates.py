# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

""""
Initial Thoughts:
 - need one extra pointer to compare(or you could compare by doing current.val == current.next.val)
 - after deleting the node have to skip the pointer to the next next node

Edge Cases:
 - empty input
 



"""""

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        if head.next == None:
            return head
        anss = current = head
        nextll = current.next
       
        while current:
            if(current.val == nextll.val):
                current.next = nextll.next
                nextll = nextll.next
                print(current)
                print(nextll)
            current = current.next
            if(nextll):
                if nextll.next:
                    nextll = nextll.next
        if(anss.next): 
            if(anss == anss.next.val):
                anss.next = None
        return anss