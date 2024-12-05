class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # step 1: check if both string contain the same length ignoring _

        if start.replace("_","") != target.replace("_",""):
            return False

        # step 2: check movement for "L" pieces

        i, j = 0, 0
        while i < len(start) and j < len(target):
            while i < len(start) and start[i] != "L":
                i += 1
            while j < len(target) and target[j] != "L":
                j += 1
            
            # if one index reaches the end other does not, mismatch case
            if i == len(start) or j == len(target):
                break
            
            # L in start can only move left
            if i < j:
                return False
            
            i += 1
            j += 1


        # Step 3: Check movement of "R" pieces
        i , j = 0, 0
        while i < len(start) and j < len(target):
            while i < len(start) and start[i] != "R":
                i += 1
            while j < len(target) and target[j] != "R":
                j += 1
            
            # if one index reaches the end other does not, mismatch case
            if i == len(start) or j == len(target):
                break
            
            # L in start can only move right
            if i > j:
                return False
            
            i += 1
            j += 1

        return True

