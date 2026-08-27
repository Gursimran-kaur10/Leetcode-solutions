class Solution(object):
    def isArraySpecial(self, nums):
        result=True
        for i in range(1,len(nums)):
            if nums[i]%2==nums[i-1]%2:
                result=False
                break
        return result
        
