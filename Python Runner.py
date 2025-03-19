"""
UTC ID: TYV379
Name: joseph Edwards
Date: 06/20/2021
"""

import csv

with open('times.csv' , mode='w', newline='') as scores:
    writing_object = csv.writer(scores)
    x = int(input('How many runners are competing? '))
    for i in range(x):
        first_name = input('Please enter the first name of the runner: ')
        last_name = input('Please enter the last name for this runner: ')
        time_one = float(input('What was there first lap time? '))
        time_two = float(input('What was there second lap time? '))
        time_three = float(input('What was there final lap time? '))
        
        writing_object.writerow([first_name,last_name,time_one,time_two,time_three])
        
    print('\nYour file has Printed!')