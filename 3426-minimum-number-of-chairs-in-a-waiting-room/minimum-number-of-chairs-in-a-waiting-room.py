class Solution:
    def minimumChairs(self, s: str) -> int:
        count = a_chairs = 0
        for c in s:
            if c == 'E':
                a_chairs += 1
            else:
                a_chairs -= 1
            count = max(count,a_chairs) 

        return count
