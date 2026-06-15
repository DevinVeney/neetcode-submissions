class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join([char for char in s if char.isalnum()])
        c = cleaned.lower()
        left = 0
        right = -1
        
        for letters in range(len(c)//2):            
            if c[left] != c[right]:
                return False
            else:
                left += 1
                right -= 1
        return True        
        
