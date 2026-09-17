class Solution(object):
    def isAlienSorted(self, words, order):
        rank = {}

        for i in range(len(order)):
            rank[order[i]] = i

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            j = 0

            while j < min(len(word1), len(word2)):
                if word1[j] != word2[j]:
                    if rank[word1[j]] > rank[word2[j]]:
                        return False
                    break

                j += 1

            # word1 is longer but word2 is its prefix
            if j == len(word2) and len(word1) > len(word2):
                return False

        return True
