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

'''
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = m - 1          # Last actual element of nums1
        j = n - 1          # Last element of nums2
        k = m + n - 1      # Last position of nums1

        # Compare from the end and place the larger element
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1

            k -= 1

        # If nums2 still has elements, copy them
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
'''
