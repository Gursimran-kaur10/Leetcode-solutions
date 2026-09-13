class Solution(object):
    def minSubArrayLen(self, target, nums):
        minimum=float('inf')
        left=0
        right=0
        sum=0
        for right in range(len(nums)):
            sum +=nums[right]

            while sum>=target:
                length=(right-left)+1
                minimum=min(minimum,length)

                sum-=nums[left]
                left+=1
        if ans==float('inf'):
            return 0
        else:
            return minimum

            
