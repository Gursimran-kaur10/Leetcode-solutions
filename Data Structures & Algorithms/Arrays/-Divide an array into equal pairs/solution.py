class Solution(object):
    def divideArray(self, nums):
        freq={}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        for i in freq.values():
            if i%2!=0:
                return False
        return True

        
