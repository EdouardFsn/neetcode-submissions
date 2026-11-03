class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = dict()
        final_count = 0
        for n in nums:
            values[n] = 1
        for n in nums:
            temp_count = 1
            t = n
            if (t-1 not in values):
                while ( t+1 in values):
                    temp_count += 1
                    t += 1
            if (temp_count > final_count):
                final_count = temp_count
        return final_count            


        