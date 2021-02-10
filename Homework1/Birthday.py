# Laura Moreno
# PSID = 1763766
# pront user to enter information
print('Birthday Calculator')
print('Current day')
month_1 = input('Month:')
day_1 = int(input('Day:'))
year_1 = int(input('Year:'))
print('Birthday')
month_2 = input('Month:')
day_2 = int(input('Day:'))
year_2 = int(input('Year:'))
# output age in years
age = year_1 - year_2
print('You are', age, 'years old.')
if month_1 == month_2 and day_1 == day_2:
    print('Happy Birthday')
