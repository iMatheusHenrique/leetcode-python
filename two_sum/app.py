from typing import Dict,Union

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
