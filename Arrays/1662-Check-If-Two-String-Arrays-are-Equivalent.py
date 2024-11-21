class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # (INPUTS) -> word1: List[str] & word2: List[str]
        # (OUTPUT) -> boolean (True if they have the same string, otherwise False)
        # (ASSUMPTIONS):
        #                   1. Arrays can be concatenated to form the string.
        #                   2. It should be case senstive
        # (EXAMPLE):
        #           1. ["aaa", "zzz", "ccc"], ["aaazzz", "ccc"]
        # (STEPS):
        #           1. Join the elements inside the arrays to form a string
        #           2. Compare the strings
        #           3. Return the value of the comparison (True or False)
        # (COMPLEXITY):
        #               Time Complexity: O(n + m), because join loops over
        #                                all elements
        #               Space Complexity: O(n + m), because two arrays are saved
        word1_string = "".join(word1[:]) # "aaa" + "zzz" + "ccc" = "aaazzzccc"
        word2_string = "".join(word2[:]) # "aaazzz" + "ccc" = "aaazzzccc"
        return (word1_string == word2_string) # True