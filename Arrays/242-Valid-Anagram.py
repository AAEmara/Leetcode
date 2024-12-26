class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        (INPUT):
            s: str
            t: str
        (OUTPUT):
            True or False
        (EXAMPLE):
            s = "anagram", t = "nagaram"
        (ASSUMPTIONS and CONSTRAINTS):
            1. s and t are lowercase English letters
            2. s and t are not empty and have at least 1 character
        (STEPS):
            1.1 calculate the length of s and t
            1.2 check if the length of s and t is equal or not
                1.2.1 if not, return false
            1.3 initialize an empty object, s_frequency
            1.4 loop over the array s:
                1.4.1 if the letter in s is in s_frequency:
                    2.1.1 increment the frequency of the letter in s_frequency
                1.4.2 else:
                    2.2.1 initialize the frequecy of the letter to 1
            1.5 Loop over the array t:
                1.5.1 check if the value corresponding to the letter > 0:
                    1.5.1.1 decrement the frequency of the letter in s_frequency
                1.5.2 else:
                    return false
            1.6 return true
        (ANALYSIS):
            Time Complexity: O(n + m) ~ O(n)
            Space Complexity: O(n + m) ~ O(n)
        """
        len_s = len(s)
        len_t = len(t)
        if len_s != len_t:
            return False
        s_frequency = dict()

        for letter in s:
            if s_frequency.get(letter, 0):
                s_frequency[letter] += 1
            else:
                s_frequency[letter] = 1
        
        for letter in t:
            if s_frequency.get(letter, 0) > 0:
                s_frequency[letter] -= 1
            else:
                return False
        return True
