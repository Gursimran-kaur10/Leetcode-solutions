class Solution(object):
    def threeSum(self, nums):
        ans=[]
        nums.sort()
        
        for i in range (len(nums)-2):
            left=i+1
            right=len(nums)-1
            if i>0 and nums[i]==nums[i-1]:
                continue
            while left<right:
                total=nums[i]+nums[left]+nums[right]
                if total==0:
                    ans.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left < right and nums[left] == nums[left - 1]:
                        left+=1   # to avoid again adding same numbers
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total<0:
                    left+=1
                else:
                    right-=1
        return ans

        
