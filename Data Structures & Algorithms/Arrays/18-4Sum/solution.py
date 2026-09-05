class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        ans = []
        n = len(nums)

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 3, n):
                if j < n - 1 and nums[j] == nums[j + 1]:
                    continue

                left = i + 1
                right = j - 1

                while left < right:
                    total = nums[i] + nums[left] + nums[right] + nums[j]

                    if total == target:
                        ans.append([nums[i], nums[left], nums[right], nums[j]])

                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    elif total < target:
                        left += 1

                    else:
                        right -= 1

        return ans
