class Solution(object):
    def specialArray(self, nums):
        
        for x in range(1,len(nums)+1):
            count=0
            i=0
            while i<len(nums):
                if nums[i]>=x:
                    count+=1
                
                i+=1
            if count==x:
                return x
        
        return -1
            
