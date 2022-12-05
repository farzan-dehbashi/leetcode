class Solution:
        def twoSum(self, nums: List[int], target: int):
            lp = 0
            rp = len(nums) - 1
            while True:
                if nums[lp] + nums[rp] == target:
                    return [lp+1, rp+1]
                elif nums[lp] + nums[rp] < target:
                    lp += 1
                else:
                    rp -= 1
