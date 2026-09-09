class Solution(object):
    def sortArrayByParity(self, nums):
        # Two pointers:
        # left starts from the beginning
        # right starts from the end
        left = 0
        right = len(nums) - 1

        # Continue until the pointers cross
        while left <= right:

            # If the left element is even,
            # it is already in the correct group.
            if nums[left] % 2 == 0:
                left += 1

            # If the right element is odd,
            # it is already in the correct group.
            elif nums[right] % 2 == 1:
                right -= 1

            # Otherwise:
            # nums[left] is odd
            # nums[right] is even
            # So swap them.
            else:
                nums[left], nums[right] = nums[right], nums[left]

                # Both elements are now in the correct group,
                # so move both pointers.
                left += 1
                right -= 1

        return nums
