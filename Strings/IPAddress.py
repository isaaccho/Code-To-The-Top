class Solution:
    def defangIPaddr(self, address: str) -> str:
        
        # #brute force waym,O(n)
        # res = address.split('.')
        # ans = ""
        # check = 0
        # a1 =len(res)
        # for x in res:
        #     check = check + 1
        #     if check == a1:
        #         ans = ans + x
        #         return ans
        #     ans = ans + x + "[.]"
            
        #one liner, O(n)
        return address.replace(".","[.]")
        
  
        
        