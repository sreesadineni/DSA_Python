class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res= []
        stack = []

        def backtrack(openParam,closedParam):
            if openParam == closedParam == n:
                res.append("".join(stack))

            if openParam < n:
                stack.append("(")
                backtrack(openParam+1,closedParam)
                stack.pop()

            if openParam > closedParam:
                stack.append(")")
                backtrack(openParam,closedParam+1)
                stack.pop()

        backtrack(0,0)
        return res


        