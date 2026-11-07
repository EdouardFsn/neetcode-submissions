class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_rect = 0
        current_rect = 0
        stack = collections.deque()
        length = len(heights)

        for i, h in enumerate(heights):
            index = i
            while(stack and stack[-1][1] > h):
                index = stack[-1][0]
                current_rect = (i - index) * stack[-1][1]
                if (current_rect > max_rect):
                    max_rect = current_rect
                stack.pop()
            stack.append((index, h))
        while (stack):
            current_rect = (length - stack[-1][0] ) * stack[-1][1]
            stack.pop()
            if (current_rect > max_rect):
                    max_rect = current_rect
        return max_rect


        