class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)
        maxLeft[0] = 0
        maxRight[len(height)-1] = 0
        water = 0
        for i in range(1,len(height), 1):         
            maxLeft[i] = max(maxLeft[i-1], height[i-1])
        for i in range(len(height)-2, -1, -1): 
            maxRight[i] = max(maxRight[i+1], height[i+1])
        for i in range(len(height)):
            i_water = min(maxLeft[i],maxRight[i]) - height[i]
            if (i_water > 0):
                water += i_water
        return water






        