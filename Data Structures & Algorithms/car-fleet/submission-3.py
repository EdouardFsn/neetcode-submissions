class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not position:
            return 0
        map_time = {}      
        output = 1
        for i in range(len(position)):
            map_time[position[i]] = (target - position[i]) / speed[i]
        position.sort()
        current_time = map_time[position[-1]]
        for i in range(len(position)-2, -1 , -1):
            if map_time[position[i]] > current_time:
                output += 1
                current_time = map_time[position[i]]
        return output



        