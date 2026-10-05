class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0
        
        for char in s:
            if char == '(':
                stack.append(score)
                score = 0
            else:
                # if the outer is nested i.e "))" we multiply with 2 , if the outer is "()" we just add 1 as score has become zero in prev step
                score = stack.pop() + max(2 * score, 1)
                
        return score
