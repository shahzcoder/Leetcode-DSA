class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        s_words = [word[::-1] for word in words]
        return ' '.join(s_words)
