class Solution(object):
    def subsetXORSum(self, nums):
        def solve(i,xor):
            if i==len(nums):
                return xor
            include=solve(i+1,nums[i]^xor)
            exclude=solve(i+1,xor)
            return include+exclude
        return solve(0,0)    
