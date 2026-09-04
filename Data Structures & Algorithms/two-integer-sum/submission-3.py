class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hsh = {}

        for i,n in enumerate(nums) :
            diff = target - n
            if diff in hsh:
                return [hsh[diff], i]
            else:
                hsh[n] = i
            