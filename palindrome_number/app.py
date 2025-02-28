"""
Given an integer x, return true if x is a 
palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        original = x
        reversed = 0

        while x != 0:
            reversed = reversed * 10 + x % 10
            x = x//10
        return original == reversed

x = -101
x = 101
x = 121

solution_obj = Solution()
result = solution_obj.isPalindrome(x=x)

print(f"Given {x=}, we have {result=}")
