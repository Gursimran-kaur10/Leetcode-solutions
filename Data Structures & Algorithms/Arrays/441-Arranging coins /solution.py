class Solution(object):
    def arrangeCoins(self, n):
        i=1
        count=0
        while(n>=i):
            n=n-i
            count+=1
            i+=1
        return count
        
