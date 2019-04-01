# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

input_date = list(map(int, input().split(' ')))
print(input_date)
index_day = calendar.weekday(input_date[2],input_date[0],input_date[1])-2
print(index_day)
print(calendar.day_name[index_day].upper())