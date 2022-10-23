def is_leap(years):
    if years % 4 == 0:
        if years % 100 == 0:
            if years % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(the_year, the_month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(the_year):
        month_days[1] = 29
    return month_days[the_month - 1]


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

