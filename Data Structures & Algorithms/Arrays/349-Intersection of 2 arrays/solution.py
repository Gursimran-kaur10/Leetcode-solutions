'''class Solution(object):
    def intersection(self, nums1, nums2):
        return list(set(nums1)&set(nums2))
        '''
# 2 approaches

class Solution(object):
    def intersection(self, nums1, nums2):
        if len(nums1)<len(nums2):
            small=nums1
            large=nums2
        else:
            small=nums2
            large=nums1
        s=set(small)
        arr=[]
        for i in range(len(large)):
            if large[i] in s and large[i] not in arr:
                arr.append(large[i])
        return arr
