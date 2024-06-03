def is_year_leap(year):
    return year % 4 == 0


year = 2024
leap_year = is_year_leap(year)

print(f"Год {year}: {leap_year}")
