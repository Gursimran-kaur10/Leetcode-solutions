class Solution(object):
    def stringMatching(self, words):
        result=[]
        for i in range(len(words)):
            for j in range(len(words)):
                if words[i]!=words[j] and words[i] in words[j]:
                    result.append(words[i])
                    break
        return result
