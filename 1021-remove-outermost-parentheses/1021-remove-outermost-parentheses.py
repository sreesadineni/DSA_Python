class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        if len(s) == 1:
            return ""
        open = 0
        resstr = ""
        for index in range(len(s)):
            if s[index] == "(":
                open +=1
                if (open == 1):
                    start = index
            else:
                 open = max(open-1,0)
                 if (open == 0):
                    end = index +1
                    result = s[start:end]
                    resstr += result[1:-1] 
        return resstr
                    

        