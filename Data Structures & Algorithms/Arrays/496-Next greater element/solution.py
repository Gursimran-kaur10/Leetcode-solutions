class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        result=[]
        for num in nums1:
            index=nums2.index(num)
            ans=-1
            
            for j in range(index+1,len(nums2)):
                if nums2[j]>num:
                    ans=nums2[j]
                    break
            result.append(ans)
        return result

#if timecomplexity is issue then use monotonic stack transverse nums2 removing smaller element from stack if stack eleemnt then -1 else top one is next graeter maintaing hashmap then transverse nums1 find anser for each element from hashmap
        
