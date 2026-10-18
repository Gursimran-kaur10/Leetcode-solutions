class Solution(object):
    def minimumSize(self, nums, maxOperations):
        left=1
        right=max(nums)
        ans=0

        while left<=right:
            mid=(left+right)//2
            operations=0

            for balls in nums:
                operations+=(balls-1)//mid
            if operations <= maxOperations:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans
        
        
