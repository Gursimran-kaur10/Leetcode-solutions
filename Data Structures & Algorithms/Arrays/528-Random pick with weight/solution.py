import random
import bisect


class Solution:

    def __init__(self, w):
        # Create an empty list to store prefix sums
        self.prefix = []

        # Variable to keep track of the running total
        total = 0

        # Go through every weight in the given list
        for weight in w:

            # Add the current weight to the total
            total += weight

            # Store the current prefix sum
            self.prefix.append(total)

        # Store the total sum of all weights
        self.total = total

    def pickIndex(self):

        # Generate a random number between 1 and total weight
        target = random.randint(1, self.total)

        # Find the first prefix sum that is >= target
        # This gives us the required index
        return bisect.bisect_left(self.prefix, target)
