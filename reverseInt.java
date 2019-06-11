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

            while(x!=0)
            {
                int temp = x%10;
                x = x/10;
        if (ans > Integer.MAX_VALUE/10||ans ==Integer.MAX_VALUE/10 && temp >7) 
        {
            return 0;
        }
        if (ans < Integer.MIN_VALUE/10||ans ==Integer.MIN_VALUE/10 && temp<-8) 
        {return 0;
        }
                                ans = ans*10 +temp;

            }
    
            if(sign)
            {
                ans = ans*-1;
            }



        
            
        
        
        return ans;
    }
}