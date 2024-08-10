class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for o in operations:
            if o == '+':
                record.append(record[-1] + record[-2])
            elif o == 'D':
                record.append(record[-1] * 2)
            elif o == 'C':
                record.pop()
            else:
                record.append(int(o))
            
        return sum(record)    