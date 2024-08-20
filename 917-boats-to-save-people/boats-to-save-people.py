class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        i = 0
        j = len(people) - 1
        boats = 0
        
        while i <= j:
            if people[i] + people[j] <= limit:
                boats += 1
                i += 1
                j -= 1
            else:
                boats += 1
                j -= 1

        return boats