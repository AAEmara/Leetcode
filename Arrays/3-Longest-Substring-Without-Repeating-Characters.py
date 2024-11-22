class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
          (INPUTS): s: str = "mamamia"
          (OUTPUT): max_substring_len: int = 3
          (ASSUMPTIONS):
                        1. The are repeating characters in the string
                        2. A string may contain english letters, digits, symbols,
                           and spaces
                        3. We don't have to return the sub-string, just its length
          (STEPS):
                    1. Intialize an array to hold the current sub-string with []
                    2. Create a variable to hold the max length of a substring
                    3. One pointer looping over the string from the beginning
                    4. Compare the character at hand if it's in the current array
                    5. While the char is in the array then calculate the length of 
                       the items in the current substring array
                    6. Compare the current length of the substring array with the
                       max length of the substring array
                    7. Remove the first occurence of the char from the 
                       current substring array
                    8. If not, Add the character to the current substring
                    8. Move the pointer forward
                    8. Repeat from 3 to 7
                    9. Return the max length of the substrings
         (ANALYSIS):
                    Time Complexity: O(n * m)
                                    n: Length of the string (Outer loop)
                                    m: Length of the substring (Checking the array)
                                        m = n at worst case (substring = string)
                                    c: Length of the substring to shift after
                                       deleting the first character
                                       c = n-1 at worst case O(n-1) ~ O(n)
                                    Worst Case Scenario O(n^3)
        """
        # "mamamia"
        # "mammamia"
        current_substring: List[str] = []
        max_substring_length = 0
        # i = 0, s[i] = 'm', [] => ['m'], max_len = 0
        # i = 1, s[i] = 'a', ['m'] => ['m', 'a'], max_len = 0
        # i = 2, s[i] = 'm', ['m', 'a'] => ['a', 'm'], max_len = 2
        # i = 3, s[i] = 'm', ['a', 'm'] => ['m', 'm'], max_len = 2
        # i = 3, s[i] = 'm', ['m', 'm'] => ['m'], max_len = 2
        # i = 4, s[i] = 'a', ['m'] => ['m', 'a'], max_len = 2
        # i = 5, s[i] = 'm', ['m', 'a'] => ['a'], max_len = 2
        # i = 5, s[i] = 'm', ['a'] => ['a', 'm'], max_len = 2
        # i = 6, s[i] = 'i', ['a', 'm'] => ['a', 'm', 'i'], max_len = 2
        # i = 7, s[i] = 'a', ['a', 'm', 'i'] => ['m', 'i'], max_len = 3
        # i = 7, s[i] = 'a', ['m', 'i'] => ['m', 'i', 'a'], max_len = 3
        # max(3, 3) => return 3

        
        # O(n) for the for loop
        for i in range(len(s)):
            # O(n) at worst case
            while s[i] in current_substring:
                current_len = len(current_substring) # O(1)
                max_substring_length = max(max_substring_length, current_len) # O(1)
                del current_substring[0] # O(n-1) because del from beginning
            current_substring.append(s[i]) # O(1) for adding at the end
        return max(max_substring_length, len(current_substring))