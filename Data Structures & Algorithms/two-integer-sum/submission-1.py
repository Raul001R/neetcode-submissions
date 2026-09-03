class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            
            hsh = {}

            for i, num in enumerate(nums):
                diff = target - num
                if diff in hsh:
                    return [hsh[diff], i]
                else:
                    hsh[num] = i