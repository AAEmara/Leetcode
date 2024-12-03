class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        """
        Time Complexity: O(2n)
        Space Complexity: O(1)
        """
        nums_sum = 0
        left_nums_sum = 0
        for num in nums:
            nums_sum += num

        """
        EXAMPLE:
        nums = [2, 3, -1, 8, 4]
        i   nums[i]     left_nums_sum   nums_sum
        0       2           2               16-2=14
        1       3           5               14-3=11
        2       -1          4               11--1=12
        3       8           4               12-8=4      -> return i -> return 3
        nums = [1, -1, 4]
        0       1           1               4-1=3
        1       -1          0               3--1=4
        2       4           0               4-4=0       -> return i -> return 2
        nums = [2, 5]
        0       2           2               7-2=5
        1       5           5               5-5=0
        return -1
        """

        for i in range(len(nums)):
            nums_sum -= nums[i]
            if left_nums_sum == nums_sum:
                return i # returning the current index as middleIndex
            left_nums_sum += nums[i]
        return -1