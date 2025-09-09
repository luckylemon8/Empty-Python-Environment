input_date = input("Input a date: ")

day = input_date[0:2]
month = input_date[3:5]
year = input_date[6:]

day = int(day)
month = int(month)
year = int(year)

monthname = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
daysinmonth = ["31", "28", "31", "30", "31", "30", "31", "31", "30", "31", "30", "31"]

valid_date = True

if month < 0 or month > 12:
    print("invalid month. month must be between 1 and 12.")
    valid_date = False
elif day < 0 or day >= int(daysinmonth[month-1]):
    print("Invalid day. must be between 0 and " + (daysinmonth[month-1]))
    valid_date = False

if len(str(year)) != 4:
    print("Year is not four numbers.")
    valid_date = False

if valid_date:
    print((str(day) + " " + (monthname[month-1]) + " " + str(year)))


