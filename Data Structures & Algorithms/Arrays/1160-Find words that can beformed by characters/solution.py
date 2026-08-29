class Solution(object):
    def countCharacters(self, words, chars):
        char_freq=Counter(chars)
        ans=0
        for word in words:
            word_freq=Counter(word)
            if all(word_freq[c]<=char_freq[c] for c in word_freq):
                ans+=len(word)
        return ans
        
