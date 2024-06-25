class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        events = defaultdict(int)

    # Record the birth and death events
        for birth, death in logs:
            events[birth] += 1
            events[death] -= 1

    # Sort the years and compute the population
        max_population = 0
        current_population = 0
        earliest_year = 0

        for year in sorted(events.keys()):
            current_population += events[year]
            if current_population > max_population:
                max_population = current_population
                earliest_year = year

        return earliest_year