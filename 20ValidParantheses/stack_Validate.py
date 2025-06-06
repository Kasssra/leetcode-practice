class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        for i in s:
            if i in "({[":
                stack.append(i)
            elif not stack:
                return False
            elif i == "}":
                if stack.pop() != "{":
                    return False
            elif i == "]":
                if stack.pop() != "[":
                    return False
            elif i == ")":
                if stack.pop() != "(":
                    return False
            
        if stack:
            return False
        return True