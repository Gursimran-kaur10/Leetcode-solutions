class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        count=Counter(arr1)
        ans=[]
        for x in arr2:
            if x in count:
                for _ in range(count[x]):
                    ans.append(x) 
                del count[x]
        for x in sorted(count):
            for _ in range(count[x]):
                ans.append(x)
        return ans
        
