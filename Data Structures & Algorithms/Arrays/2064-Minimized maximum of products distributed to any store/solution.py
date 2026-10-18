class Solution(object):
    def minimizedMaximum(self, n, quantities):
        left = 1
        right = max(quantities)
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            stores = 0

            for q in quantities:
                stores += (q + mid - 1) // mid

            if stores <= n:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans
