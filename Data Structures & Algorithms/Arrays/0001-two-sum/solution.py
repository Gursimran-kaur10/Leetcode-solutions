class Solution(object):
    def twoSum(self, nums, target):
     mp={} #hashmap
     for i in range(len(nums)):
        complement=target-nums[i]
        if complement in mp:
            return [mp[complement],i]
        else:
            mp[nums[i]]=i
        

        
