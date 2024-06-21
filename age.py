import datetime

date_today = datetime.date.today()
dob = input('What is your date of birth? (YYYY-MM-DD): ')
year = int(dob[:4])
month = int(dob[5:7])
day = int(dob[8:10])
date_of_birth = datetime.date(year, month, day)
approx_age = date_today.year - date_of_birth.year
if date_today.month < date_of_birth.month:
    age = approx_age -1
elif date_today.month == date_of_birth.month and date_today.day < date_of_birth.day:
    age = approx_age -1
else:
    age = approx_age

print(age)