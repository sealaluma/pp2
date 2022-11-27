from datetime import datetime, time, date

date_inp1 = input('Enter first date formatted as YYYY-MM-DD: ').split('-')
year, month, day = [int(item) for item in date_inp1]
date1 = date(year, month, day)

date_inp2 = input('Enter second date formatted as YYYY-MM-DD: ').split('-')
year, month, day = [int(item) for item in date_inp2]
date2 = date(year, month, day)

diff = (date2 - date1)
diff = diff.days * 24 * 3600
print(diff)