class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.insert(0, c)
            elif len(stack) > 0:
                if c == ')':
                    if stack[0] == '(':
                        stack.pop(0)
                    else:
                        return False
                if c == ']':
                    if stack[0] == '[':
                        stack.pop(0)
                    else:
                        return False

                if c == '}':
                    if stack[0] == '{':
                        stack.pop(0)
                    else:
                        return False
            else:
                return False
            
                
                # stack += c
        return len(stack) == 0
        