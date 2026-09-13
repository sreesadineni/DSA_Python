class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowercase = s.lower()
        finalResponse = ""
        reverseResponse = ""
        for char in lowercase:
            if char.isalnum():
                finalResponse = finalResponse + char
                reverseResponse = char + reverseResponse
        return finalResponse == reverseResponse