class Solution:
    def minimumMountainRemovals(self, nums):
        n = len(nums)

        # Longest Increasing Subsequence ending at each index
        left = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    left[i] = max(left[i], left[j] + 1)

        # Longest Decreasing Subsequence starting at each index
        right = [1] * n
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, i, -1):
                if nums[j] < nums[i]:
                    right[i] = max(right[i], right[j] + 1)

        min_removals = n - 3

        # Try every possible peak
        for i in range(1, n - 1):
            if left[i] > 1 and right[i] > 1:
                mountain_length = left[i] + right[i] - 1
                removals = n - mountain_length
                min_removals = min(min_removals, removals)

        return min_removals
