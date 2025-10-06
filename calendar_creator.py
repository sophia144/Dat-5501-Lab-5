#asking for user input
num_days = int(input('How many days are there in this month?\n'))
start_day = int(input('Which day does this month start on? Please respond with a number (1 = Monday ... 7 = Sunday)\n'))
print('\n')

#sets up the week template and gaps in the first week
calendar_string = "M   T   W   T   F   S   S\n"
calendar_string += (start_day - 1) * "--  "

#sets up variables for loop
current_date = 1
current_day = start_day

#loops for each day of the month
for day in range(0, num_days):

    #adds the number of the date to the calendar
    calendar_string += (str(current_date) + '    ')[0:4]

    #starts a new line if it is at the end of the week
    if current_day == 7:
        calendar_string += '\n'
        current_day = 1
    else:
        current_day += 1

    #increments the date by one
    current_date += 1

#outputs the result
print(calendar_string + '\n')
