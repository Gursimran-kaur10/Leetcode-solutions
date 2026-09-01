class Solution(object):
    def wiggleSort(self, nums):
        for i in range(1, len(nums)):
            if i % 2 == 1:
                # odd index: previous <= current
                if nums[i - 1] > nums[i]:
                    nums[i - 1], nums[i] = nums[i], nums[i - 1]
            else:
                # even index: previous >= current
                if nums[i - 1] < nums[i]:
                    nums[i - 1], nums[i] = nums[i], nums[i - 1]
