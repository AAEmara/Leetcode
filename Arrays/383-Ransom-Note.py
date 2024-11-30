class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
            (INPUTS):
                ransomNote: str
                magazine: str
            (OUTPUTS):
                is_constructed: bool
            (EXAMPLE):
                ransomNote = "lol"
                magazine = "hello"
            (ASSUMPTIONS and CONSTRAINTS):
                1. The INPUTS are lowercase English letters.
                2. The INPUTS are at least 1.
                3. The letters in `magazine` could be sufficient or not to form the
                   `ransomNote` string
                4. Each letter in `magazine` could be used once in `ransomNote`
                5. If letters in `magazine` can construct `ransomNote`, the it
                   will return True, otherwise False.
            (SOLUTIONS):
                1. BRUTE FORCE:
                    1.1 Loop on the chars in ransomNote to be constructed
                        1.1.1 Loop on chars in magazine
                            1.1.1.1 If the char in ransomNote doesn't exist in
                                    magazine, return False
                                    (cannot construct magazine)
                            1.1.1.2 If the char was found in magazine, remove it
                                    from the magazine array (cut it off)
                        1.1.2 When the inner loop on magazine's chars finishes,
                              move on in the outer loop of ransomNote
                    1.2 The outer loop finishes and we return True
                2. HASH TABLE:
                    2.1 Loop on the chars in magazine to create the Hash Table
                        2.1.1 If char in Hash Table
                            2.1.1.1 Add one to the value of the corresponding char
                                    as a key
                        2.1.2 otherwise
                            2.1.2.1 Intitialize the char as a key with value 1
                    2.2 Loop on the chars in ransomNote
                        2.2.1 If char of ransomNote in magazine's Hash Table
                            2.2.1.1 Decrease the value of the corresponding char
                        2.2.2 If char does not exist in magazine's Hash Table
                            2.2.2.1 return False
                    2.3 return True
            (TIME COMPLEXITY):
                BRUTE FORCE:
                    n: length of ransomNote, m: length of magainze
                    Time Complexity: O(n*m*m) (Outer, inner loops, and array del)
                    Space Complexity: O(m) (The new array of magazine)
                HASH TABLE:
                    n: length of ransomNote, m: length of magainze
                    Time Complexity: O(n+m) (magazine's loop and ransomNote's loop)
                    Space Complexity: O(m) (creating a Hash Table of length m at
                                            worst case)
        """
        # Hash Table Solution
        char_table = dict()
        """
        EXAMPLE: ransomNote = "lol", magazine = "hello"
        """
        for char in magazine:
            if char not in char_table:
                char_table[char] = 0 # Initialize it with 0 value
            char_table[char] += 1 # increase the value of the char frequency by 1
        """
        char char_table
        'h'     {h: 1}
        'e'     {h: 1, e: 1}
        'l'     {h: 1, e: 1, l: 1}
        'l'     {h: 1, e: 1, l: 2}
        'o'     {h: 1, e: 1, l: 2, o: 1}
        char_table = {h: 1, e: 1, l: 2, o: 1}
        """
        for char in ransomNote:
            if char not in char_table or char_table[char] < 1:
                return False # can not construct the ransomNote
            char_table[char] -= 1
        """
        char char_table
        'l'     {h: 1, e: 1, l: 1, o: 1}
        'o'     {h: 1, e: 1, l: 1, o: 0}
        'l'     {h: 1, e: 1, l: 0, o: 0}
        char_table = {h: 1, e: 1, l: 0, o: 0}
        """
        return True # we constructed the ransomNote from the chars in magazine