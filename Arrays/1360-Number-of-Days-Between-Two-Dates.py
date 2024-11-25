class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        """
            (COMPLEXITY):
                Time Complexity: O(n)
                Space Complexity: O(1)
        """
        days_inbetween = 0
        date1_arr = date1.split("-") # [Year, Month, Day]
        date2_arr = date2.split("-")

        days_to_year1 = self.get_year_days(
            int(date1_arr[0]), int(date1_arr[1]), int(date1_arr[2]))
        days_to_year2 = self.get_year_days(
            int(date2_arr[0]), int(date2_arr[1]), int(date2_arr[2]))
        return abs(days_to_year1 - days_to_year2)

    def get_year_days (self, year: int, month: int, day: int) -> int:
        """ Calculates the number of days from 1900 till the given year.
        """
        days_to_year = 0
        for current_year in range(1900, year):
            is_leap = self.is_leap_year(current_year)
            if (is_leap):
                days_to_year += 366
            else:
                days_to_year += 365
        for current_month in range(1, month + 1):
            is_leap = self.is_leap_year(year)
            if (current_month == month):
                days_to_year += day
            else:
                days_to_year += self.get_month_days(current_month, is_leap)
        return days_to_year

    def is_leap_year (self, year: int) -> int:
        """ Checks if the year is a leap year or not.
        Returns:
            1 if True
            0 if False
        """
        if (year % 4 == 0):
            if (year % 100 == 0):
                if (year % 400 == 0):
                    return 1
                return 0
            return 1
        return 0

    def get_month_days (self, month: int, is_leap: int) -> int:
        """ Gets the number of days inside a month.
        """
        if month in [9, 4, 6, 11]:
            return 30
        elif month == 2 and is_leap:
            return 29
        elif month == 2 and (not is_leap):
            return 28
        return 31