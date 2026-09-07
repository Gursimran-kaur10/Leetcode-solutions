class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        
        count=0
        window_sum=sum(arr[:k])

        i=0
        while i+k<=len(arr):
            if window_sum/k>=threshold:
                count+=1
            if i+k<len(arr):
                window_sum-=arr[i]
                window_sum+=arr[i+k]
            i+=1
        return count
        
