class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        # Create a dictionary to keep count of all the characters in t
        map = defaultdict(int)
        for char in t:
            map[char] += 1
        
        counter = len(map)  # Number of unique characters in t that need to be in the window
        
        begin, end = 0, 0  # Two pointers to define the window
        head = 0  # Start position of the minimum window
        min_len = float('inf')  # Length of the minimum window
        
        while end < len(s):
            char = s[end]
            if char in map:
                map[char] -= 1
                if map[char] == 0:
                    counter -= 1
            end += 1
            
            while counter == 0:
                # Try to shrink the window from the left
                temp_char = s[begin]
                if temp_char in map:
                    map[temp_char] += 1
                    if map[temp_char] > 0:
                        counter += 1
                
                # Update the minimum window
                if end - begin < min_len:
                    min_len = end - begin
                    head = begin
                
                begin += 1
        
        if min_len == float('inf'):
            return ""
        
        return s[head:head + min_len]