class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) -1

        while( l <= r):
            k = (l + r) // 2 
            if ( nums[k] == target):
                return k
            if (nums[k] >= nums[l]):
                if ( nums[l] <= target and target <= nums[k]):
                    r = k-1
                else:
                    l = k+1
            else:
                if ( nums[l] <= target or target <= nums[k]):
                    r = k-1
                else:
                    l = k+1


        return -1
        