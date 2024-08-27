from collections import defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        result = []
        if len(p) > len(s):
            return result
        
        # Create a dictionary to count characters in p
        char_count = defaultdict(int)
        for char in p:
            char_count[char] += 1
        
        counter = len(char_count)
        begin, end = 0, 0
        
        while end < len(s):
            char = s[end]
            
            if char in char_count:
                char_count[char] -= 1
                if char_count[char] == 0:
                    counter -= 1
            
            end += 1
            
            while counter == 0:
                temp_char = s[begin]
                
                if temp_char in char_count:
                    char_count[temp_char] += 1
                    if char_count[temp_char] > 0:
                        counter += 1
                
                if end - begin == len(p):
                    result.append(begin)
                
                begin += 1
        
        return result
