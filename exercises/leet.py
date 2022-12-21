class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        i:int = 0
        while i < (len(nums) - 1):
            x: int = i + 1
            while x < (len(nums) - 1):
                if nums[i] + nums[x] == target:
                    return [i, x]
                x += 1
            i += 1
        return []
            