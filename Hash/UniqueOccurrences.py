class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import Counter
        
        ctr = Counter(arr)
        check = ctr.values()
        
        
        #checks if there are any duplicates in the list
        if len(check) == len(set(check)):
            return True
           
        else:
            return False
        
