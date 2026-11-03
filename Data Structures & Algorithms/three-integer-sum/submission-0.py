class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        final_list = []
        values = dict()
        temp_sum = 0
        already_set = set()
        for i in range(len(nums)):
            if (nums[i] not in values):
                values[nums[i]] = i
        for i in range(len(nums)):
            for j in range(i+1, (len(nums)),1 ):
                temp_sum = nums[i] + nums[j]
                missing_value = 0 - temp_sum
                if (missing_value in values):
                    if(values[missing_value] != i and values[missing_value] !=j ):
                        temp = [nums[i], nums[j], missing_value]
                        temp.sort()
                        attempt = tuple(temp)
                        if (attempt not in already_set):
                            already_set.add(attempt)
                            final_list.append(attempt)
        return final_list      
        