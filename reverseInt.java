class Solution {
    public int reverse(int x) {
        boolean sign = false;
        int ans=0;

 
            if(x<0)
            {
                 sign = true;
                x = x*-1;

            }
        
            int length=Integer.toString(x).length();

            for(int i=0;i<length;i++)
            {
                ans = ans*10;
                ans = ans + x%10;
                x = x/10;
            }
    
            if(sign)
            {
                ans = ans*-1;
            }


         if (ans > Integer.MAX_VALUE/10||ans ==Integer.MAX_VALUE/10) 
        {
            ans = 0;
        }
        if (ans < Integer.MIN_VALUE/10||ans ==Integer.MIN_VALUE/10) 
        {
            ans = 0;
        }
        
            
        
        
        return ans;
    }
}