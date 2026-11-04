class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        hashmap_test = {}
        hashmap_w = {}

        for i in s1:
            hashmap_test[i] = 1 + hashmap_test.get(i, 0)

        for right in range(len(s2)):
            hashmap_w[s2[right]] = 1 + hashmap_w.get(s2[right], 0)
            if (right - left +1 > len(s1)):
                hashmap_w[s2[left]] -= 1
                if ( hashmap_w[s2[left]] == 0):
                    del hashmap_w[s2[left]]
                left += 1
            if (hashmap_w == hashmap_test):
                return True
        return False

        