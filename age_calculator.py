from datetime import datetime
from datetime import time
import datetime

def check_birthdate(year, month, day):
	#if (year>2019 or month<1 or month>12 or day<1 or day>31):
	birthdate=datetime.date(year, month, day)
	if (birthdate>datetime.date.today()):
		return False
	else:
		return True    
        
                # write code here


def calculate_age(year, month, day):
	birthdate=datetime.date(year, month, day)
	thisYear = datetime.date.today().year
	#birthdayYear= birthdate.date.year


	age=(thisYear-birthdate.year)
	print ("You are %d age old" %(age,))
    # write code here

def main():
	# write main code here
	year = int (input ("Enter the year: "))
	month=int (input("Enter the month as a number: "))
	day= int(input("Enter the day: "))
	if(check_birthdate(year, month, day)==False):
		print("The date is invalid")
	else:
		calculate_age(year, month, day)


if __name__ == '__main__':
	main()
