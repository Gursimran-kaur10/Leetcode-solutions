class Solution:
    def getFinalState(self, nums, k, multiplier):
        for _ in range(k):
            minimum = min(nums)
            index = nums.index(minimum)

            nums[index] *= multiplier

        return nums
