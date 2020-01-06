class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        from collections import Counter
        
        ctr = Counter(A)
        #n = len(A)//2
        
        for keys in ctr:
            if ctr.get(keys) == len(A)/2:
                return keys

        