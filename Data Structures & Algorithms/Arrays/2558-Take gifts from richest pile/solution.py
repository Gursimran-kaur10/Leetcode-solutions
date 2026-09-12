class Solution:
    def pickGifts(self, gifts, k):
        for _ in range(k):
            gifts.sort()

            largest = gifts.pop()
            gifts.append(int(largest ** 0.5))

        return sum(gifts)
