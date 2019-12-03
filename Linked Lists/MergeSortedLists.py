# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None



"""-	Initial thoughts:
o	Both lists are sorted, increasing order
o	Have to compare node from each list at a time and then add it to ensure the final list is also sorted
o	Need multiple pointers


-	Possible solutions: 
o	Have two pointers that point to two different lists
o	Have one more pointer that can keep merging the list by changing the pointer



-	Edge cases:
o	When both lists are empty
	Return null
o	When one list is empty
	Return the list that is not empty
o	When the list doesn’t come sorted
	This would not be possible since the lists are sorted but if so, sort each list first, and then merge them"""



class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        point1 = l1 #pointer to the first list
        point2 = l2 #pointer to the second list
        
        
        if(point1 == None and point2):
            return point2
        if(point2 == None and point1):
            return point1
        if(point1 == None and point2 == None):
            return None
        
        
        #check the first value of two nodes and get the lower one
        if(point1.val<=point2.val):
            anss = point1
            final_ans = anss
            if(point1):
                point1 = point1.next
        elif(point1.val>point2.val):
            anss = point2
            final_ans = anss
            if(point2):
                point2 = point2.next
                    
        #merging the two lists until one of them is None            
        while(point1 and point2)!= None:
            if(point1.val<=point2.val):
                anss.next = point1
                anss = anss.next
                if(point1):
                    point1 = point1.next
            elif(point1.val>point2.val):
                anss.next = point2
                anss = anss.next
                if(point2):
                    point2 = point2.next

        if(point1):
            anss.next = point1
            point1 = point1.next
        if(point2):
            anss.next = point2
            point2 = point2.next
        

        return(final_ans)
            


            
        


        
        

        

        
        
