class Solution(object):
    def numIdenticalPairs(self, nums):
        mp={}
        count=0

        for i in nums:
            if i in mp:
                count+=mp[i]
            mp[i]=mp.get(i,0)+1
            
        return count
        
        
