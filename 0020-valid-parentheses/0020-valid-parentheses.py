class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s)<= 1:
            return False
        for param in s:
            if param == "}" and len(stack)>0:
                if stack.pop() == "{":
                    continue
                else:
                    return False
            if param == ")" and len(stack)>0:
                if stack.pop() == "(":
                    continue
                else:
                    return False
            if param == "]" and len(stack)>0:
                if stack.pop() == "[":
                    continue
                else:
                    return False
            stack.append(param)
        if len(stack) > 0:
            return False
        return True