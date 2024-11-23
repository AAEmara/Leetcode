class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring_set = set() # Holds current substring characters
        # j is the second pointer for the current character
        i = 0 #  The first pointer as the pivoting character
        """
        Example: (It contains sparse and consecutive repeating characters)
            "mammamia" 0 -> 7 (8 characters long)
            substring, i, j, {}, max
            m        , 0, 0, {'m'}, 1
            ma       , 0, 1, {'m', 'a'}, 2
            mam      , 0, 2, {'m', 'a'}, 2
            am       , 1, 2, {'a', 'm'}, 2
            amm      , 1, 3, {'a', 'm'}, 2
            mm       , 2, 3, {'m'}, 2
            m        , 3, 3, {'m'}, 2
            ma       , 3, 4, {'m', 'a'}, 2
            mam      , 3, 5, {'m', 'a'}, 2
            am       , 4, 5, {'a', 'm'}, 2
            ami      , 4, 6, {'a', 'm', 'i'}, 3
            amia     , 4, 7, {'a', 'm', 'i'}, 3
            mia      , 5, 6, {'m', 'i', 'a'}, 3
        """
        max_substring_len = 0
        for j in range(len(s)):
            while s[j] in substring_set:
                substring_set.remove(s[i]) # Removing current char from set
                i += 1 # Change the pivoting character
            substring_set.add(s[j]) # Add the current character to set
            max_substring_len = max(max_substring_len, j - i + 1)
        return max_substring_len # 0 if empty, otherwise, maximum length