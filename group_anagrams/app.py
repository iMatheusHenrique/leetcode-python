"""
Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""

import datetime
from collections import defaultdict
from typing import List, Dict
from functools import wraps

def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.datetime.now()
        duration_ms = (end_time - start_time).total_seconds() * 1000
        print(f"Execution time: {func.__name__}: {duration_ms:.5f} ms")
        return result
    return wrapper


class Solution(object):
    @measure_time
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result: Dict[str, List[str]] = defaultdict(list)
        for idx, name in enumerate(strs):
            sorted_name: str = ''.join(sorted(name))
            result[sorted_name].append(name)
        return list(result.values())

solution_obj = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
result = solution_obj.groupAnagrams(strs)
print(f"""Given {strs=},\nwe have the {result=}""")
