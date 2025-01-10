from collections import Counter
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        maxFreq = Counter()
        for word in words2:
            wordFreq = Counter(word)
            for char in wordFreq:
                maxFreq[char] = max(maxFreq[char], wordFreq[char])

        result = []
        for word in words1:
            wordFreq = Counter(word)
            if all(wordFreq[char] >= maxFreq[char] for char in maxFreq):
                result.append(word)

        return result