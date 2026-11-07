class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first_index = 0
        last_index = len(nums)-1
        split = (first_index + last_index) // 2

        while(first_index <= last_index):
            if(nums[split] == target ):
                return split
            elif (nums[split] < target):
                first_index = split+1
            elif (nums[split] > target):
                last_index = split-1
            split = (first_index + last_index) // 2
        return -1
            


        