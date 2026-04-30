class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        tot_rows = len(matrix)
        tot_cols = len(matrix[0])
        start = 0
        end = tot_rows - 1
        while end >= start:
            mid = start + (end - start) // 2
            mid_row = matrix[mid]
            # print(mid_row)
            if mid_row[0] <= target and mid_row[-1] >= target:
                # print("finding in", mid_row)
                s = 0
                e = tot_cols - 1
                while e >= s:
                    m = s + (e-s)//2
                    mm = mid_row[m]
                    if mm == target:
                        return True
                    if mm > target:
                        e = m - 1
                    else:
                        s = m + 1
                return False
            if mid_row[0] > target:
                end = mid - 1
            else:
                start = mid + 1
        return False