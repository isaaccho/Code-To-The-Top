# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


""""
Initial Thoughts:
- palindrome reads the same forward and backwards
- need two pointers
- have to check first and last node and see if it's the same, and then keep moving inwards 

Edge Cases:
- empty input


Possible Solutions:
- find out the half point of the linked list, reverse the second half


"""

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if(head):
            #steady = head
            curr = head
            length = 0
            even = 0


            #finding the length of the linked list
            while curr:
                curr = curr.next
                length = length + 1

            if(length%2 ==0):
                even = 1
            halfpt = length//2

            #setting curr back to the beggining
            curr = head


            #moving curr to halfway point of the list 
            while halfpt>0:
                curr = curr.next
                halfpt = halfpt -1

            prev = curr
            steady = curr.next
            curr = curr.next
            prev.next = None

            dummy = head

            #reverse the second half of the list
            while steady:
                steady = steady.next
                curr.next = prev
                prev = curr
                curr = steady


            if even==1:
                while(prev):
                    if prev.val == dummy.val:
                        prev = prev.next
                        dummy = dummy.next

                    else:
                        return False

                return True

            else:
                while(prev.next):
                    if prev.val == dummy.val:
                        prev = prev.next
                        dummy = dummy.next

                    else:
                        return False

                return True
            
        else:
            return True
        
        
            
        

        