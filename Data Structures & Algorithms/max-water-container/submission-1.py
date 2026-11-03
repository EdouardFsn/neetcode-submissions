class Solution:
    def maxArea(self, heights: List[int]) -> int:
        pointer_a = 0
        pointer_b = len(heights)-1
        max_volume = 0
        while (pointer_a != pointer_b ):
            smallest_border = min(heights[pointer_a], heights[pointer_b])
            temp_volume = smallest_border * (pointer_b - pointer_a)
            if ( temp_volume > max_volume):
                max_volume = temp_volume
            if (smallest_border == heights[pointer_a] ):
                pointer_a += 1 
            else:
                pointer_b -= 1 
        return max_volume
        