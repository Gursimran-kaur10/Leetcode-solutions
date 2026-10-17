class Solution(object):
    def maximumCandies(self, candies, k):
        left = 1
        right = max(candies)
        ans = 0

        while left <= right:
            mid = (left + right) // 2

            children = 0

            for pile in candies:
                children += pile // mid

            if children >= k:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
