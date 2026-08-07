class Solution(object):
    def longestMountain(self, arr):
        if len(arr)<3:
            return 0
        maxLen=0
        for i in range(1,len(arr)-1):
            if arr[i-1]<arr[i]>arr[i+1]:
                left=i
                right=i
                while left>0 and arr[left-1]<arr[left]:
                    left-=1
                while right<len(arr)-1 and arr[right]>arr[right+1]:
                    right+=1
                length=(right-left)+1
                maxLen=max(maxLen,length)
        return maxLen
            

        
