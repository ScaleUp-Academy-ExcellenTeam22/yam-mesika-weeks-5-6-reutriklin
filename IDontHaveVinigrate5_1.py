from datetime import date
import datetime
import random

date_entry = input('Enter a date in YYYY-MM-DD format ')
year1, month1, day1 = map(int, date_entry.split('-'))
date1 = datetime.date(year1, month1, day1)
date_entry = input('Enter another date ')
year2, month2, day2 = map(int, date_entry.split('-'))
date2 = datetime.date(year2, month2, day2)
time_between_dates = date1 - date2
days_between_dates = abs( time_between_dates.days)
random_number_of_days = random.randrange(days_between_dates)
random_date = min(date1,date2) + datetime.timedelta(days=random_number_of_days)
print(random_date)
if random_date.weekday()==0:
    print("אין לי ויניגרט כיוון שאני הולך למכולת רק בימי שני ואני צרכן כבד של רוטב ויניגרט!")