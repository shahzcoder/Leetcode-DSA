class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_alt = 0
        highest_alt = current_alt

        for alt in gain:
            current_alt = current_alt + alt
            highest_alt = max(highest_alt, current_alt)

        return highest_alt
