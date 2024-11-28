class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        (INPUTS):
            s: str

        (OUTPUTS):
            is_palindrome: bool

        (ASSUMPTIONS and CONSTRAINTS):
            1. Convert all uppercase letters into lowercase letters.
            2. Remove all non-alphanumeric characters
            3. The word is read the same from the start to the end as
               from the end to the start.
            4. Alphanumeric characters include characters and numbers.
            5. An empty string could be read back and forth, so it's a palindrome
        
        (EXAMPLE):
            s = "Rar, aN, na; rar"
            is_palindrome = True
        (STEPS):
            1. Create an array of alphanumerals
            2. lowercase the given string
            3. Loop over the array and if a character is not available in
            the previously array, remove it.
            4. Move with two pointer and compare each character until they reach
            half of the array.
            5. if the loop is didn't finish return False, otherwise return true.
        """
        num_start: int = ord('0')
        num_end: int = ord('9')
        lower_start: int = ord('a')
        lower_end: int = ord('z')
        upper_start: int = ord('A')
        upper_end: int = ord('Z')
        conversion_diff: int = lower_start - upper_start
        """
        lower_start upper_start conversion_diff
            100         1           99
            1           100         -99
        To convert from upper to lower
        case_I 1 + 99 = 100 # returned to lower value
        case_II 100 + -99 = 1 # returned to lower value
        """
        new_s: str = ""
        """
        i       s                     s[i]    chr(char_num)     new_s
        0   "Rar, aN, na; rar"        R         r               "r"
        1   "Rar, aN, na; rar"        a         a               "ra"
        2   "Rar, aN, na; rar"        r         r               "rar"
        3   "Rar, aN, na; rar"        ,         ,               "rar"
        4   "Rar, aN, na; rar"        " "      " "              "rar"
        5   "Rar, aN, na; rar"        a         a               "rara"
        6   "Rar, aN, na; rar"        N         N               "raran"
        7   "Rar, aN, na; rar"        ,         ,               "raran"
        8   "Rar, aN, na; rar"        " "       " "             "raran"
        9   "Rar, aN, na; rar"        n         n               "rarann"
        10   "Rar, aN, na; rar"        a         a              "raranna"
        11   "Rar, aN, na; rar"        ;         ;              "raranna"
        12  "Rar, aN, na; rar"        " "       " "             "raranna"
        13  "Rar, aN, na; rar"        r         r               "rarannar"
        14  "Rar, aN, na; rar"        a         a               "rarannara"
        15  "Rar, aN, na; rar"        r         r               "rarannarar"
        """
        # Converting any uppercase letter into a lowercase letter.
        for i in range(len(s)):
            char_num: int = ord(s[i])
            if char_num >= lower_start and char_num <= lower_end:
                pass
            elif char_num >= num_start and char_num <= num_end:
                pass
            elif char_num >= upper_start and char_num <= upper_end:
                char_num += conversion_diff # replacing upper with lower
            else:
                continue # the char is not alphanumeric, so skip.
            new_s += chr(char_num)

        """
        new_s: "rarannarar"
        len(new_s)//2 = 10 // 2 = 5
        i   j   new_s[i]    new_s[j]
        0   -1      r           r
        1   -2      a           a
        2   -2      r           r
        3   -3      a           a
        4   -4      n           n
        """
        j: int = -1
        for i in range(len(new_s)//2):
            if new_s[i] != new_s[j]:
                return False
            j -= 1
        return True