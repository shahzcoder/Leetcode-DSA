class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        p1 , p2 = 0, 0
        index = 1

        while p1 < len(sentence):
            if sentence[p1] == searchWord[p2]:
                if p2 == 0 and (p1 == 0 or sentence[p1 - 1] == " "):
                    p2 += 1
                elif p2 > 0:
                    p2 += 1
                if p2 == len(searchWord):
                    return index
            else:
                if sentence[p1] == ' ':
                    index += 1
                    p2 = 0
                elif p2 > 0:
                    p2 = 0
                
            p1 += 1
        
        return -1
                    