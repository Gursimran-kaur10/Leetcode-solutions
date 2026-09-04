class Solution(object):
    def findDifference(self, nums1, nums2):
        set1=set(nums1)
        set2=set(nums2)

        result=[]
        result.append(list(set1-set2))
        result.append(list(set2-set1))
        return result

        
