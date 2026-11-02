class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += s + "ç"
        return encoded


    def decode(self, s: str) -> List[str]:
        decoded = []
        temp_decoded = ""
        for c in s:
            if ( c == "ç"):
                decoded.append(temp_decoded)
                temp_decoded = ""
            else:
                temp_decoded += c
        return decoded
                
