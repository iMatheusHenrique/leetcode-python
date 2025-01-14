"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""

from typing import Dict,Union, DefaultDict

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        Result = 
        given input: [2,7,11,15]
        giver output: 9

        hasher = {
            7: 0,
            ...,
        }
        returns:  
        
        """
        hasher: Dict[int, int] = {}
        for idx, num in enumerate(nums):
            idx_num_in_hasher: Union[str|None] = hasher.get(num)

            if idx_num_in_hasher is not None:
                return [idx_num_in_hasher, idx]

            hasher[target-num] = idx

solution_obj = Solution()
nums = [2,7,11,15]
target = 9
result = solution_obj.twoSum(nums, target)
print(f"""Given {nums=} and {target=},\nwe have the {result=}""")
