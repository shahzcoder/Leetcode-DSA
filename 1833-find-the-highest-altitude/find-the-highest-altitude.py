class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        gain.insert(0,0)
        n = len(gain)

        for i in range(2, n):
            gain[i] = gain[i - 1] + gain[i]

        return max(gain)

