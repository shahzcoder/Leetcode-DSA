class Solution:
    def myAtoi(self, s: str) -> int:
        # contraint for 32bit signed integer range
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        # Step 1: ignore leading white spaces manually 
        n = len(s)
        i = 0
        while i < n and s[i] == " ":
            i += 1

        # Step 2: Check if sting is empty after skipping white spaces
        if i == n:
            return 0

        # Step 3: Determine the Sign
        sign = 1
        if s[i] in ('-','+'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        # Step 4: Convert characters to integers
        result = 0
        while i < n and '0' <= s[i] <= '9':
            result = result * 10 + (ord(s[i]) - ord('0')) # Convert char to int using ASCII

            # Step 5: Handle overflow
            if sign * result < INT_MIN:
                return INT_MIN
            if sign * result > INT_MAX:
                return INT_MAX

            i += 1 
    
        return sign * result