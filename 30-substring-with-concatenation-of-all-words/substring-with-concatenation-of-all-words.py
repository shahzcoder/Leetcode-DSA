from collections import defaultdict
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_length = len(words[0])
        num_words = len(words)
        substring_length = word_length * num_words
        s_length = len(s)

        if s_length < substring_length:
            return []

        word_count = defaultdict(int)
        for word in words:
            word_count[word] += 1

        result = []

        # Iterate over each possible starting index
        for i in range(word_length):
            begin, end = i, i
            current_count = defaultdict(int)
            count = 0

            while end + word_length <= s_length:
                word = s[end:end + word_length]
                end += word_length

                if word in word_count:
                    current_count[word] += 1
                    if current_count[word] <= word_count[word]:
                        count += 1

                    # Shrink the window from the left if there are too many of the current word
                    while current_count[word] > word_count[word]:
                        left_word = s[begin:begin + word_length]
                        current_count[left_word] -= 1
                        if current_count[left_word] < word_count[left_word]:
                            count -= 1
                        begin += word_length

                    # If the count of matched words equals the number of words, add the start index
                    if count == num_words:
                        result.append(begin)

                        left_word = s[begin:begin + word_length]
                        current_count[left_word] -= 1
                        if current_count[left_word] < word_count[left_word]:
                            count -= 1
                        begin += word_length

                else:
                    # Reset the window if the word is not in the list of words
                    current_count.clear()
                    count = 0
                    begin = end

        return result
