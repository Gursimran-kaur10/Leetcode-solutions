class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        total = sum(nums)

        if total % k != 0:
            return False

        target = total // k

        nums.sort(reverse=True)

        buckets = [0] * k

        def backtrack(index):
            if index == len(nums):
                return True

            num = nums[index]

            for i in range(k):
                if buckets[i] + num <= target:
                    buckets[i] += num

                    if backtrack(index + 1):
                        return True

                    buckets[i] -= num

                if buckets[i] == 0:
                    break

            return False

        return backtrack(0)
