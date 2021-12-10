import datetime

enter_date = int(input("Enter Date "))
if len(str(enter_date)) > 2:
    enter_date = int(input("You have enter an invalid date. Please Enter again (Date) "))
    if len(str(enter_date)) > 2:
        raise Exception("Sorry, You have enter an invalid date")

enter_month = int(input("Enter month "))
if len(str(enter_month)) > 2:
    enter_month = int(input("You have enter an invalid month. Please Enter again (month) "))
    if len(str(enter_month)) > 2:
        raise Exception("Sorry, You have enter an invalid month")

enter_year = int(input("Enter Year "))
if len(str(enter_year)) > 4:
    enter_year = int(input("You have enter an invalid date. Please Enter again (Year) "))
    if len(str(enter_year)) > 2:
        raise Exception("Sorry, You have enter an invalid Year")

current_date = datetime.datetime.now()

if current_date.year >= enter_year:
    if current_date.month >= enter_month:
        if current_date.day >= enter_date:
            age_year = current_date.year - enter_year
            age_month = current_date.month - enter_month
            age_day = current_date.day - enter_date

            if age_month >= 0:
                if age_day >= 0:
                    print("")
                else:
                    age_day = abs(age_day)
            else:
                age_month = abs(age_month)
            print("You are", age_year, "Years", age_month, "Month", age_day, "Days old")
        else:
            print("You have enter an Invalid Date of Bitrh (Date)")
    else:
        print("You have enter an Invalid Date of Bitrh (Month)")
else:
    print("You have enter an Invalid Date of Bitrh (Year)")
