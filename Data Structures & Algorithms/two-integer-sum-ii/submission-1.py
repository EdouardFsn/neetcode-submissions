class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first_index = 0
        last_index = len(numbers)-1
        sum = 0
        while ( numbers[first_index] + numbers[last_index] != target):
            sum = numbers[first_index] + numbers[last_index]
            if (sum < target):
                first_index += 1
            if (sum > target):
                last_index -= 1         
        return [first_index+1, last_index+1]