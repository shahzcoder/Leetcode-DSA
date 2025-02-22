class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        def countWordsInSentence(sentence):
            count = 0
            for char in sentence:
                if char == ' ':
                    count += 1

            return count + 1
        
        maxWords = 0
        for sentence in sentences:
            maxWords = max(maxWords, countWordsInSentence(sentence))

        return maxWords