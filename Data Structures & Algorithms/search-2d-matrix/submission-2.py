class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        first_index_row = 0
        last_index_row = len(matrix) -1
        mid_index_row = (first_index_row + last_index_row) // 2

        while ( first_index_row <= last_index_row ):
            mid_index_row = (first_index_row + last_index_row) // 2
            if (target == matrix[mid_index_row][0] ):
                return True
            elif (target < matrix[mid_index_row][0]):
                last_index_row = mid_index_row-1
            elif (target > matrix[mid_index_row][0]):
                first_index_row = mid_index_row+1

        good_row = matrix[last_index_row]
        left = 0
        right = len(good_row) -1

        while left <= right:
            mid = (left + right) // 2
            if good_row[mid] == target:
                return True
            elif good_row[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
 




        