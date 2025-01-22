class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i == '(' or i =='{' or i =='[':
                stack.append(i)
            else:
                if not stack:
                    return False
                t_item = stack.pop()

                if (t_item == '(' and i ==')') or (t_item == '{' and i =='}') or (t_item == '[' and i ==']'):
                    continue
                else:
                    return False
        
        return not stack