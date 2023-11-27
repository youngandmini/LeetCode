class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        open_brackets = {"(", "{", "["}
        
        for bracket in s:
            if bracket in open_brackets:
                stack.append(bracket)
                continue
            
            if bracket == ")":
                if not stack:
                    return False
                if stack.pop() != "(":
                    return False
                continue
            if bracket == "}":
                if not stack:
                    return False
                if stack.pop() != "{":
                    return False
                continue
            if bracket == "]":
                if not stack:
                    return False
                if stack.pop() != "[":
                    return False
                continue
        
        if stack:
            return False
        return True