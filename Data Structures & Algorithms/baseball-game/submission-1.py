class Solution:
    def isInteger(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def calPoints(self, operations: List[str]) -> int:
        mem = []
        for op in operations:
            print(mem)
            if self.isInteger(op):
                mem.append(int(op))
            elif op == "+":
                mem.append(mem[-1] + mem[-2])
            elif op == "D":
                mem.append(2 * mem[-1])
            elif op == "C":
                mem.pop()

        return sum(mem)