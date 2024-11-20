class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # (INPUT) nums: List[int] = [2,3,4,8]
        # (INPUT) target: int = 6
        # (OUTPUT) indicies: List[int] = [0, 2]
        # ASSUMPTIONS: 1. Exactly one solution
        #                 (e.g., nums = [2,3,2,1]; target = 4, indicies = [0, 2])
        #              2. You can't use the same element twice 
        #                 (e.g., nums = [2,3,2,1]; target = 4, indicies = [0, 0]XXX)
        #              3. You can return the answer in any order
        #                 (e.g., nums = [2,3,2,1]; target = 4, indicies = [2, 0])
        #              4. You cannot have only one index in the output
        #              5. The numbers are not sorted
        # Suggested Solutions: Two Nested Loops, Time Complexity: O(n^2)
        # [2, 3, (4), 8], target = 6
        # [(6), 2, 4, 6], target = 6
        # [(3), 2, 4], target = 6
        hash_table = dict() #6: 0, (2): 1, 
        # 1. For loop on the numbers in the array
        for i in range(len(nums)):
            # 2. Subtract the number from the target and access the hash table
            #    to see if there is a value there or not.
            #    (Key = number, value = index)
            complement = target - nums[i] # 4, 3, 2
            if complement in hash_table:
                # 3. If the complement was found in the hash table, then return
                #    the value of the key and then current index in an array.
                return [hash_table[complement], i]
            # 4. If not, add the current number in the hash table
            hash_table[nums[i]] = i
            # 5. repeat from 1 to 4