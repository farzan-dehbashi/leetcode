class Solution(object):
    def twoSum(self, nums, target):
        num_dict = dict()
        for index ,num in enumerate(nums):
            if not num in num_dict.keys():
                num_dict[num] = index
        for index, num1 in enumerate(nums):
            sub = target - num1
            if sub in nums and (num_dict[sub] != index):
                return [num_dict[sub],  index]
