class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        total_time = 0
        mink = (r+l) // 2


        while ( r >= l):
            k = (r+l) // 2
            for p in piles:
                total_time += -((-p)//k)
            if (total_time > h ):
                l = k+1
            else:
                r = k-1
                mink = k
            total_time =0
        return mink


        