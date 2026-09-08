class Solution(object):
    def maxFrequency(self, nums, k):
        nums.sort()

        left = 0
        total = 0
        ans = 0

        for right in range(len(nums)):
            total += nums[right]

            # Cost to make every element in the window
            # equal to nums[right]
            cost = nums[right] * (right - left + 1) - total

            while cost > k:
                total -= nums[left]
                left += 1

                cost = nums[right] * (right - left + 1) - total

            ans = max(ans, right - left + 1)

        return ans
