class Solution(object):
    def minimumIndex(self, nums):
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        dominant=0
        n=len(nums)
        total=0
        for num in freq:
            if freq[num]>n//2:
                dominant=num
                total=freq[num]
                break
        left_count=0
        for i in range(n-1):
            if nums[i]==dominant:
                left_count+=1
            right_count=total-left_count
            left_length=i+1
            right_length=n-i-1

            if (left_count>left_length//2 and right_count>right_length//2):
                return i
        return -1
