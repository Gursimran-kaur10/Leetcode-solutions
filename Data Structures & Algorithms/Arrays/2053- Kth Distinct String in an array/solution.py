class Solution(object):
    def kthDistinct(self, arr, k):
        mp={}
        count=0

        for s in arr:
            if s in mp:
                mp[s]+=1
            else:
                mp[s]=1

        for s in arr:
            if mp[s]==1:
                count+=1

                if count==k:
                    return s
        return ""
        
