from functools import cmp_to_key

class Solution(object):
    def largestNumber(self, nums):

        # Convert every number into a string
        # Example: [3, 30, 34] -> ["3", "30", "34"]
        nums = map(str, nums)

        # This function decides which number should come first
        def compare(a, b):

            # Check which order creates the larger number
            # Example: a="3", b="30"
            # "330" > "303", so 3 should come first
            if a + b > b + a:
                return -1

            # If b+a is larger, b should come first
            elif a + b < b + a:
                return 1

            # Both orders are equal
            return 0

        # Sort using our custom comparison function
        nums = sorted(nums, key=cmp_to_key(compare))

        # Special case:
        # If the largest number is "0", all numbers are zero
        # So return only "0", not "000..."
        if nums[0] == "0":
            return "0"

        # Join all strings together
        # Example: ["9","5","34","3","30"] -> "9534330"
        return "".join(nums)
