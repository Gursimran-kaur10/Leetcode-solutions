class Solution(object):
    def findDisappearedNumbers(self, nums):
        nums.sort()
        n = len(nums)
        result = []

        for i in range(1, n + 1): # we need to chcek from 1 to n ie n+1 doesn't included
            if i not in nums:
                result.append(i)

        return result
