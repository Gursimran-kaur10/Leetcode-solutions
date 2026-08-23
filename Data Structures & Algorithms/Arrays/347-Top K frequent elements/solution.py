class Solution(object):
    def topKFrequent(self, nums, k):
        mp = {}

        # Count frequency
        for num in nums:
            mp[num] = mp.get(num, 0) + 1

        # Sort keys according to their frequency
        arr = sorted(mp, key=mp.get, reverse=True)

        # Return top k
        return arr[:k]
        
