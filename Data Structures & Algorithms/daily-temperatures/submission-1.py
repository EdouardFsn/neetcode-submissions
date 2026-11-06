class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        queue_index = collections.deque()
        queue = collections.deque()
        for i in range(len(temperatures)):
            while queue and queue[-1] < temperatures[i]:
                queue.pop()
                index_pop = queue_index.pop()
                index_diff = i - index_pop
                output[index_pop] = index_diff
            queue.append(temperatures[i])
            queue_index.append(i)
        return output

        

        