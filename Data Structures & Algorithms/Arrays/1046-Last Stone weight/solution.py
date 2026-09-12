class Solution:
    def lastStoneWeight(self, stones):
        while len(stones) > 1:
            stones.sort()

            x = stones.pop()      # largest
            y = stones.pop()      # second largest

            if x != y:
                stones.append(x - y)

        return stones[0] if stones else 0

'''
import heapq

class Solution:
    def lastStoneWeight(self, stones):
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)

            if x != y:
                heapq.heappush(stones, -(x - y))

        return -stones[0] if stones else 0
'''
