class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)

        open = 0
        for ch in s:
            if ch == '(' or ch == '*':
                open += 1
            else:
                open -= 1

            if open < 0:
                return False

        close = 0
        for i in range(n - 1, -1, -1):
            if s[i] == ')' or s[i] == '*':
                close += 1
            else:
                close -= 1

            if close < 0:
                return False

        return True