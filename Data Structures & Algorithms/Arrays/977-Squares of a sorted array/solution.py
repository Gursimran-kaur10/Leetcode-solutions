class Solution(object):
    def sortedSquares(self, nums):
        ans=[0]*len(nums)
        k=len(ans)-1
        
        left=0
        right=len(nums)-1
        while left<=right:
            if nums[left]*nums[left]>nums[right]*nums[right]:
                ans[k]=nums[left]*nums[left]
            
                left+=1
            else:
                ans[k]=nums[right]*nums[right]
                right-=1
            k-=1
        return ans
        
