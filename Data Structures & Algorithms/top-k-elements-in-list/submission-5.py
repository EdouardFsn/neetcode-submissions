class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = dict()
        freq = [[] for i in range(len(nums)+1)]
        for n in nums:
            if n in hashmap: 
                hashmap[n] += 1
            else: 
                hashmap[n] = 1
        for n, c in hashmap.items():
            freq[c].append(n)

        topfreq = []
        for i in range(len(freq)-1,0 ,-1):
            for n in freq[i]:
                topfreq.append(n)
                if (len(topfreq) == k):
                    return topfreq

