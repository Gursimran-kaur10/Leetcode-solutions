class Solution(object):
    def numOfSubarrays(self, arr):
        #we will use prefix sum we know odd+even=odd at each stage its odd prefix we subtract even prefix to get odd subarray if current is odd prefix it can have combination with each even one 
        prefix=0
        ans=0
        odd=0
        even=1
        MOD=10**9+7
        for i in arr:
            prefix+=i
            if prefix%2==0:
                ans+=odd
                even+=1
            else:
                ans+=even
                odd+=1
        return ans%MOD
        
