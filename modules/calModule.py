#import calendar module for calender functionalities
import calendar

def calmodule():

# Take year and Month as Input from user
    a=input("ENTER YEAR(YYYY):")
    b=input("ENTER MONTH(MM):")

# display the calendar
    print(calendar.month(int(a),int(b)))

calmodule()

