class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            
            elif stack and (char == ')' and (stack[-1] != '(') or (char == ']' and stack[-1] != '[') or (char == '}' and stack[-1] != '{')):
                return False
            
            elif not stack:
                return False
            
            else:
                stack.pop()
        return (len(stack) == 0)
        
            

            
        