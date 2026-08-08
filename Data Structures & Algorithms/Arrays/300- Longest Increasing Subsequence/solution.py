class Solution(object):
    def lengthOfLIS(self, nums):
        n=len(nums)
        l=[1]*n
        for i in range(n):
            for j in range(i):
                if nums[j]<nums[i]:
                    l[i]=max(l[i],l[j]+1)
        return max(l)
        
