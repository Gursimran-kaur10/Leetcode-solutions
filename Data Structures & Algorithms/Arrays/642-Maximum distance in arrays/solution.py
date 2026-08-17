class Solution(object):
    def maxDistance(self, arrays):
        global_min=arrays[0][0]
        global_max=arrays[0][-1]
        ans=0
        for i in range(1,len(arrays)):
            current_min=arrays[i][0]
            current_max=arrays[i][-1]

            ans=max(ans,global_max-current_min,current_max-global_min)

            global_min=min(global_min,current_min)
            global_max=max(global_max,current_max)
        return ans
        
