class Solution(object):
    def leastBricks(self, wall):
        mp = {}

        for row in wall:
            prefix = 0

            for i in range(len(row) - 1):
                prefix += row[i]

                if prefix in mp:
                    mp[prefix] += 1
                else:
                    mp[prefix] = 1

        if not mp:
            return len(wall)

        max_gap = max(mp.values())

        return len(wall) - max_gap
