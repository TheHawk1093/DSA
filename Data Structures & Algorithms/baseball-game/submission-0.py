class Solution:
    def calPoints(self, operations: List[str]) -> int:
        points = []
        for ops in operations:
            if ops == "C":
                points.pop()
            elif ops ==  "+":
                points.append(points[-1] + points[-2])
            elif ops == "D":
                points.append(points[-1]*2)
            else:
                points.append(int(ops))
        return sum(points)