class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if ( len(s) == 0 or len(s) == 1):
            return len(s)
        left = 0
        right = 0
        contained = set()
        contained.add(s[0])
        max = 0
        for i in range(1, len(s), 1):
            right = i
            while (s[i] in contained):
                contained.remove(s[left])
                left += 1
            contained.add(s[i])
            if (len(contained) > max):
                max = len(contained)
        return max
        
                


        