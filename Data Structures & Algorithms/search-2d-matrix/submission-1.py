class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m * n - 1
        while l <= r:
            med = (l + r) // 2
            val = matrix[med // n][med % n]
            if val == target:
                return True
            elif val < target:
                l = med + 1
            else:
                r = med - 1
        return False

        