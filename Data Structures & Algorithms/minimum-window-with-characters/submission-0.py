class Solution:
    def minWindow(self, s: str, t: str) -> str:

        window = {}
        target_window = {}
        res = [-1,-1]
        res_len = float("infinity")
        l = 0

        for c in t:
            target_window[c] = 1 + target_window.get(c, 0)

        have = 0
        need = len(target_window)

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if (c in target_window and window[c] == target_window[c]):
                have += 1

            while (have == need):
                if (r - l +1) < res_len:
                    res_len = (r - l +1)
                    res = [l, r]
                
                window[s[l]] -= 1
                if (s[l] in target_window and window[s[l]] < target_window[s[l]]):
                    have -= 1
                l += 1

        if res_len == float("infinity"):
            return ""
        else:
            l = res[0]
            r = res[1]
            return s[l:r+1]




         