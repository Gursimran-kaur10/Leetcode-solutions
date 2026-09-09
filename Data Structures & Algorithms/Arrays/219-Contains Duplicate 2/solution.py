class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        # Set stores elements in the current window
        seen = set()

        # Traverse the array
        for i in range(len(nums)):

            # If the current number is already in the set,
            # we have found a duplicate within distance k.
            if nums[i] in seen:
                return True

            # Add the current number to the window
            seen.add(nums[i])

            # Keep only the last k elements before the next index
            if len(seen) > k:
                seen.remove(nums[i - k])

        # No nearby duplicate found
        return False
