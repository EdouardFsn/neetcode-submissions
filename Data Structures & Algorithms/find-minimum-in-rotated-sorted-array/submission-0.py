class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = nums[0]

        while( l <= r):
            k = (l + r) // 2
            if ( nums[l] < nums[r]):
                res = min( res, nums[l])
                break
            res = min(res, nums[k])
            if (nums[k] >= nums[l]):
                
                l = k+1
            else:
                r = k-1
        return res


        