class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        hashmap = {}
        final = 0
        if ( len(s) == 0 or len(s) == 1):
            return len(s)

        
        for right in range(len(s)):
            hashmap[s[right]] = 1 + hashmap.get(s[right],0)
            while ((right - left + 1) - max(hashmap.values()) > k ):
                hashmap[s[left]] -= 1
                left += 1
            final = max(final, right - left +1 )

        return final


        