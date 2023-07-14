from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = dict()
        for index_1, number_1 in enumerate(nums):
            if target - number_1 in hash_table:
                return [hash_table[target - number_1],index_1]
            hash_table[number_1] = index_1

print(Solution().twoSum(nums=[2, 7, 11, 15], target=9))
