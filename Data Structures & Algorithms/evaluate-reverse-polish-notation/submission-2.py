class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = collections.deque()
        val1 = 0
        val2 = 0

        for i in tokens:
            if i in "+-*/": 
                val2 = stack[-1]
                stack.pop()
                val1 = stack[-1]
                stack.pop()
                if( i == '+'):
                    stack.append(val1 + val2)
                if( i == '-'):
                    stack.append(val1 - val2)
                if( i == '*'):
                    stack.append(val1 * val2)
                if ( i == '/'):
                    stack.append(int(val1 / val2))
            else:
                stack.append(int(i))

        if stack:  
            return stack[0]
        else: 
            return 0

        