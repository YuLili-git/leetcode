#给定一个二维矩阵 matrix，以下类型的多个请求：
#计算其子矩形范围内元素的总和，该子矩阵的左上角为 (row1, col1) ，右下角为 (row2, col2) 。
#实现 NumMatrix 类：
#NumMatrix(int[][] matrix) 给定整数矩阵 matrix 进行初始化
#int sumRegion(int row1, int col1, int row2, int col2) 返回左上角 (row1, col1) 、右下角 (row2, col2) 的子矩阵的元素总和。
#示例 1：
#输入: 
#["NumMatrix","sumRegion","sumRegion","sumRegion"]
#[[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]
#输出: 
#[null, 8, 11, 12]
#解释:
#NumMatrix numMatrix = new NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]]);
#numMatrix.sumRegion(2, 1, 4, 3); // return 8 (红色矩形框的元素总和)
#numMatrix.sumRegion(1, 1, 2, 2); // return 11 (绿色矩形框的元素总和)
#numMatrix.sumRegion(1, 2, 2, 4); // return 12 (蓝色矩形框的元素总和)
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), (len(matrix[0]) if matrix else 0)
        self.sums = [[0] * (n + 1) for _ in range(m)]
        _sums = self.sums

        for i in range(m):
            for j in range(n):
                _sums[i][j + 1] = _sums[i][j] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        _sums = self.sums
        total = sum(_sums[i][col2 + 1] - _sums[i][col1] for i in range(row1, row2 + 1))
        return total




# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
