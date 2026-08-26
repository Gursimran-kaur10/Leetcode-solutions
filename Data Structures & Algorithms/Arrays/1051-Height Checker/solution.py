class Solution(object):
    def heightChecker(self, heights):
        expected=sorted(heights)
#sorted used not .sort bcz sorted create copy mot change the original one to compare
        count=0

        for i in range(len(heights)):
            if heights[i]!=expected[i]:
                count+=1
        return count        
