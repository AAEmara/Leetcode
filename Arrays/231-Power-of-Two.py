class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
            Time Complexity: O(log(n))
            Space Complexity: O(1)
        """
        guess = 1 # equivalent to 2 power ZERO
        if (n == 1):
            return True
        while (guess < n):
            guess *= 2
        return guess == n