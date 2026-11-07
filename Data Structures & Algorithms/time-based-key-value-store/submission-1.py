class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append([value, timestamp])

        

    def get(self, key: str, timestamp: int) -> str:
        l = 0
        r = len(self.hashmap[key]) -1
        m = ( r + l) // 2
        res = ""

        while (l <= r):
            m = ( r + l) // 2
            if ( self.hashmap[key][m][1] == timestamp ):
                return self.hashmap[key][m][0]
            if ( self.hashmap[key][m][1] <= timestamp):
                l = m+1
                res = self.hashmap[key][m][0]
            else:
                r = m-1
        return res
            


        
