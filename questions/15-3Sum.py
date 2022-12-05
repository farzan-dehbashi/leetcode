def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        i_dict = dict()
        res_nums = list()
        for i, num in enumerate(nums):
            if not num in i_dict.keys():
                i_dict[num] = i
        sorted_nums = list(set(sorted_nums))
        for i, num in enumerate(sorted_nums):
            j = i + 1
            k = len(sorted_nums) - 1
            while j < k:
                if sorted_nums[i] + sorted_nums[j] + sorted_nums[k] == 0:
                    res_nums = res_nums + [i_dict[sorted_nums[i]], i_dict[sorted_nums[j]], i_dict[sorted_nums[k]]]

                elif sorted_nums[j] + sorted_nums[k] > -1 * sorted_nums[i]:
                    k -= 1
                else:
                    j += 1
        return res_nums


