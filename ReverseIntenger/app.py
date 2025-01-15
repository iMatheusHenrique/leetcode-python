"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1
"""
class Solution(object):
    def reversePositiveNumber(self, number):
        reversed = 0
        while number != 0:
            reversed = reversed * 10 + number % 10
            number = number//10
        return reversed

    def reverse(self, x):
        is_x_negative = x<0

        x = x*-1 if is_x_negative else x
        result = -1 if is_x_negative else 1
        reverse_result = self.reversePositiveNumber(x)
        final_result = (result * reverse_result) if reverse_result.bit_length() < 32 else 0
        return final_result


solution_obj = Solution()
x = -1234

result = solution_obj.reverse(x=x)
print(f"""given {x=}, we have {result=}""")
