class Solution(object):
    def merge(self, nums1, m, nums2, n):
        k = 0
        arr = [0] * (m + n)
        l = 0
        r = 0

        while l < m and r < n:
            if nums1[l] < nums2[r]:
                arr[k] = nums1[l]
                l += 1
            else:
                arr[k] = nums2[r]
                r += 1
            k += 1

        while l < m:
            arr[k] = nums1[l]
            l += 1
            k += 1

        while r < n:
            arr[k] = nums2[r]
            r += 1
            k += 1

        for i in range(m + n):
            nums1[i] = arr[i]
