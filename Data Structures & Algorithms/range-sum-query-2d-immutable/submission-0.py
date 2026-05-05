class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.mem = [[0 for _ in range(n + 1)]]

        for i in range(m):
            currRow = [0]
            for j in range(n):
                currRow.append(currRow[-1] + matrix[i][j])
            for j in range(1, n+1):
                currRow[j] += self.mem[-1][j]
            self.mem.append(currRow)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.mem[row2+1][col2+1] - self.mem[row1][col2+1] - self.mem[row2+1][col1] + self.mem[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)