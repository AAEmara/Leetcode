class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums: List[int] = [1, 2, 3, 4]
        # target: int = 5
        # 2 + 3 = 5
        # indices: List[int] = [1, 2]
        # if target is 6 and the nums are [3, 1, 2], I can't use 3 twice
        # return the answer in any order
        for i in range(len(nums)):
            # i: 1
            for j in range(i + 1, len(nums)):
                # j: [2, 3, 4]
                sum = nums[i] + nums[j] # 1 + 2, 1 + 3, (1 + 4 = 5)
                if (sum == target):
                    # (1 + 4 = 5) == 5
                    return [i, j] # i: 1, j: 3 [1, 3]