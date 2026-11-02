class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        producted_list = [0] * len(nums)
        total_product = 1
        count = 0
        list_zero = []
        for n in nums:            
            if (n == 0):
                list_zero.append(count)
            else:
                total_product = total_product * n
            count += 1
        if (len(list_zero) == 1):
            producted_list[list_zero[0]] = total_product
        if (len(list_zero) == 0):
            for i in range(len(nums)):
                producted_list[i] = total_product // nums[i]
        return producted_list
            

        