#3. Write a Python program to convert a month name to a number of days.
print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")

# Request input from the user to enter the name of a month and assign it to the variable 'month_name'
month_name = input("Input the name of Month: ")

# Check the input 'month_name' and provide the number of days based on the entered month
if month_name == "February":
    print("No. of days: 28/29 days")  # Display the number of days in February (28 or 29 days for leap years)
elif month_name in ("April", "June", "September", "November"):
    print("No. of days: 30 days")  # Display the number of days for months having 30 days
elif month_name in ("January", "March", "May", "July", "August", "October", "December"):
    print("No. of days: 31 days")  # Display the number of days for months having 31 days
else:
    print("Wrong month name")