class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                if stack[-1] < -asteroid:
                    stack.pop() # postive Asteroid explodes
                    continue
                elif stack[-1] == -asteroid:
                    stack.pop() #both explodes
                break
            else:
                stack.append(asteroid)
        return stack