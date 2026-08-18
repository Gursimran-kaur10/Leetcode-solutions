class Solution(object):
    def firstMissingPositive(self, nums):
        n=len(nums)
        for i in range(0,n):
            while 0<nums[i]<n and nums[nums[i]-1]!=nums[i]: #nums[i] represent current number and nums[i]-1 where it belong so until nums[nums[i]-1] have nums[i]
                nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]
        for i in range (0,n):
            if nums[i]!=i+1: #we want nums[2]=3 example 
                return i+1
        return n+1


        
