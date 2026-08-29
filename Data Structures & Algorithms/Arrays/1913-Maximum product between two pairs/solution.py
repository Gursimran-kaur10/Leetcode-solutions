class Solution(object):
    def maxProductDifference(self, nums):
        nums.sort()
        ans=nums[-1]*nums[-2]-nums[0]*nums[1]
        return ans

''' without sorting
class Solution(object):
    def maxProductDifference(self, nums):

        small1 = small2 = nums[0]
        large1 = large2 = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            # Find two smallest
            if num < small1:
                small2 = small1
                small1 = num
            elif num < small2:
                small2 = num

            # Find two largest
            if num > large1:
                large2 = large1
                large1 = num
            elif num > large2:
                large2 = num

        return large1 * large2 - small1 * small2 '''
