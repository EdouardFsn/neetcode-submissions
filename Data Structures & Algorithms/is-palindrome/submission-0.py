class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = ""
        only_alpha = ""
        for i in range(len(s)):
            if (s[i].isalnum()):
                only_alpha += s[i].lower()
        for i in range(len(only_alpha)-1, -1, -1):        
            palindrome += only_alpha[i]
        if ( only_alpha == palindrome):
            return True
        return False


        