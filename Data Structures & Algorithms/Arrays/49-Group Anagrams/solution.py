class Solution(object):
    def groupAnagrams(self, strs):
        group={}
        for s in strs:
            key="".join(sorted(s))
            if key in group:
                group[key].append(s)
            else:
                group[key]=[s]
        return list(group.values())
