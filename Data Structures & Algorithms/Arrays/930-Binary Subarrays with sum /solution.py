class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        
        def atMost(k):
            if k < 0:
                return 0

            left = 0
            count = 0
            sum = 0

            for right in range(len(nums)):
                sum += nums[right]

                while sum > k:
                    sum -= nums[left]
                    left += 1

                count += right - left + 1

            return count

        return atMost(goal) - atMost(goal - 1)
