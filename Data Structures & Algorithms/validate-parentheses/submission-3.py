class Solution:
    def isValid(self, s: str) -> bool:
        
        pairs = {
            ']' : '[',
            '}' : '{',
            ')' : '('
        }

        stack = []

        for el in s:
            if el not in pairs:
                stack.append(el)
            else:
                if not stack or stack[-1] != pairs[el]:
                    return False
                
                stack.pop()

        return len(stack) == 0


            