class Solution:
    def isValid(self, s: str) -> bool:
        waiting = collections.deque()
        for c in s:
            if ( c == '('):
                waiting.append(')')
            if ( c == '{'):
                waiting.append('}')
            if ( c == '['):
                waiting.append(']')
            if c in ')}]':
                if ( waiting and  waiting[-1] == c):
                    waiting.pop()
                else:
                    return False
        if not waiting:
            return True
        else: 
            return False
            
            



        