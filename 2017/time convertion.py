__author__ = 'Senyutina'

time = input().strip()
L= len(time)
type_time = time[(L-2)::].upper()
hour = time[:2]
print(type_time)
print(hour)
if type_time == 'PM':
    if hour == '12':
        hour = '14'
    else: hour = str(int(hour)+12)

elif type_time == 'AM':
    if hour == '12':
        hour = '00'

print(hour + time[2:(L-2)])