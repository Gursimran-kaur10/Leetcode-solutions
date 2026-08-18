class Solution(object):
    def vowelStrings(self, words, queries):
        vowels="aeiou"
        prefix=[]
        ans=[]
        count=0
        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                count+=1
            prefix.append(count)
        for left,right in queries:
            if left==0:
                ans.append(prefix[right])
            else:
                ans.append(prefix[right]-prefix[left-1])
        return ans
        
