class Solution(object):
    def minOperations(self, nums):
        count=0
        freq=Counter(nums)

        for i in freq.values():
            if i==1:
                return -1
            else:
                count+=i//3
                if i%3!=0:
                    count+=1
        return count

        
