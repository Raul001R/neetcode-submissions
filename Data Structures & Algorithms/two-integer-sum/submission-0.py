class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        hash_map = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hash_map:
                result = [hash_map[diff], i]
                return result
            else:
                hash_map[n] = i
           
