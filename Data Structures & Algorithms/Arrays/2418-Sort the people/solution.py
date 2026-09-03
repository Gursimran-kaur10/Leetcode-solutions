class Solution(object):
    def sortPeople(self, names, heights):
        mp = []

        for i in range(len(names)):
            mp.append((names[i], heights[i]))

        sorted_people = sorted(mp, key=lambda x: x[1], reverse=True)

        ans = []

        for name, height in sorted_people:
            ans.append(name)

        return ans
