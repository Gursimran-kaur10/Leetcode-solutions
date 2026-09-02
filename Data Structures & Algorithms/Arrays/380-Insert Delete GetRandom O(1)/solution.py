import random

class RandomizedSet(object):

    def __init__(self):
        self.nums = []       # Store values
        self.mp = {}         # value -> index

    def insert(self, val):
        if val in self.mp:
            return False

        # Add value at the end
        self.nums.append(val)

        # Store its index
        self.mp[val] = len(self.nums) - 1

        return True

    def remove(self, val):
        if val not in self.mp:
            return False

        # Index of value to remove
        index = self.mp[val]

        # Last element
        last = self.nums[-1]

        # Put last element at the position of val
        self.nums[index] = last
        self.mp[last] = index

        # Remove last element
        self.nums.pop()

        # Remove val from hashmap
        del self.mp[val]

        return True

    def getRandom(self):
        return random.choice(self.nums)
