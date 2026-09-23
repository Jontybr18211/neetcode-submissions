class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = [i.lower() for i in s.strip() if i.isalnum()]
        return new==new[::-1]