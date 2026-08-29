class Solution(object):
    def countConsistentStrings(self, allowed, words):
        count=0
        chars=set(allowed)
        for word in words:
            if all(c in chars for c in word):
                count+=1
        return count
        
