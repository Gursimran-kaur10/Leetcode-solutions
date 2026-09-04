class Solution(object):
    def frequencySort(self, nums):
        mp={}
        result=[]
        for num in nums:
            mp[num]=mp.get(num,0)+1
        sorted_items=sorted(mp.items(),key=lambda x:(x[1],-x[0]))

        for num,freq in sorted_items:
            result.extend([num]*freq)
        return result        
