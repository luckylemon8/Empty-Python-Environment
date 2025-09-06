input_date = input("Input a date: ")

day = input_date[0:2]
month = input_date[3:5]
year = input_date[6:10]

day = int(day)
month = int(month)
year = int(year)

monthname = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
daysinmonth = ["31", "28", "31", "30", "31", "30", "31", "31", "30", "31", "30", "31"]

if 0 < day < int(daysinmonth+1[month-1]):
    if 0 < month < 13:
        if len(year) < 5:
            print(int((daysinmonth[month-1]) + " " + (monthname[month-1]) + " " + (year)))





