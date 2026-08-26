class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        mp={}
        repeated =-1
        missing=-1
        n=len(grid)
        
        for row in grid:
            for num in row:
                if num in mp:
                    mp[num]+=1
                else:
                    mp[num]=1
        for i in range(n*n+1):
            if i not in mp:
                missing=i
            elif mp[i]==2:
                repeated=i
        return [repeated,missing]


