class Solution:

    def findDuplicate(self, nums):

        # Slow moves one step at a time
        slow = nums[0]

        # Fast moves two steps at a time
        fast = nums[0]

        # Move slow and fast until they meet
        while True:

            # Slow moves one step
            slow = nums[slow]

            # Fast moves two steps
            fast = nums[nums[fast]]

            # If they meet, a cycle exists
            if slow == fast:
                break

        # Start another pointer from the beginning
        slow = nums[0]

        # Move both pointers one step at a time
        while slow != fast:

            # Move slow one step
            slow = nums[slow]

            # Move fast one step
            fast = nums[fast]

        # The meeting point is the duplicate number
        return slow
