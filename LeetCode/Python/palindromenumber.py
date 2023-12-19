class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        
        reversed = 0
        num = x
        
        while x > 0:
            digit = x % 10
            x = x // 10
            reversed = reversed * 10 + digit
        
        return num == reversed