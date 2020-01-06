class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        from collections import Counter

        
        #Solution not using hashtable
        
        # num = 0
        # Jewel = list(J)
        # print(Jewel)
        # for element in S:
        #     if element in Jewel:
        #         num = num + 1
        # return num
        
        
        #hashtable solution
        total = 0
        
        cnt = Counter(S)
        for key in cnt:
            
            if key in J:
                total+=cnt.get(key)
        return total   