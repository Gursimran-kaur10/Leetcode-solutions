class Solution(object):
    def rotate(self, nums, k):
        n=len(nums)

        k=k%n
        nums.reverse()
        nums[:k]=nums[:k][::-1]
        nums[k:]=nums[k:][::-1]
        return nums
        
'''Reverse whole array
reverse first k eleemnt
reverse remaining eleemnt'''

        
