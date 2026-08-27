class Solution(object):
    def findLucky(self, arr):
        mp={}

        for i in arr:
            if i in mp:
                mp[i]+=1
            else:
                mp[i]=1
        ans=-1
        for i in mp:
            if i==mp[i]:
                ans=max(ans,i)
        return ans
        
