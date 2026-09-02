class Solution(object):
    def checkSubarraySum(self, nums, k):
        prefix=0
        seen={0:-1}
        for i in range(len(nums)):
            prefix+=nums[i]
            remainder=prefix%k
            if remainder in seen:
                if i-seen[remainder]>=2:
                    return True
            else:
                seen[remainder]=i
        return False
        
