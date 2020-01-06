class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import Counter
        
        ctr = Counter(arr)
        
        for keys in ctr:
            if ctr.get(keys) in keys:
                return false
            
        return true