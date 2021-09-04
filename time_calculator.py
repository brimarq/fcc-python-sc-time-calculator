class Node:
    def __init__(self, data):
        self.data = data
        self.next = None




def add_time(start, duration, weekday=''):
    print('---------------------------------')
    start_h = int(start.split()[0].split(':')[0])
    start_m = int(start.split()[0].split(':')[1])
    dur_h = int(duration.split(':')[0])
    dur_m = int(duration.split(':')[1])
    
    # Convert to 24hr time
    start_h = start_h + 12 if start.split()[1] == 'PM' else start_h

    print('start time:', f'{start_h}:{start_m}')

    dow = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    
    d = 0
    h = start_h + dur_h
    m = start_m + dur_m
    
    # Adjust if minutes overflow
    if m >= 60:
      h += 1
      m -= 60

    print('hours:', h)
    # Adjust if hours overflow
    if h >= 24:
        d = h // 24
        h %= 12

    print('hours:', h)

    # Set AM/PM
    # meridian = 'AM' if h < 12 else 'PM'
    meridian = 'PM' if h > 12 else 'AM'

    # Convert hours to 12-hr time
    h = 12 if h == 0 else h - 12 if h > 12 else h

    # Set days note if applicable 
    days = f' ({d} days later)' if d > 1 else ' (next day)' if d == 1 else ''

    if weekday:
        #! USE A CIRCULAR LINKED LIST? 
        # weekday = ', ' + weekday
        start_index = dow.index(weekday.lower())
        print('days:', d)
        if d > 7:
            d %= 7
        print('i:', start_index, 'days:', d)
        if start_index + d >= len(dow): 
            # weekday = ', ' + dow[- start_index - 1].capitalize()
            weekday = ', ' + dow[- d].capitalize()
        else:
            weekday = ', ' + dow[start_index + d].capitalize()
    

    new_time = f'{str(h)}:{str(m).zfill(2)} {meridian}{weekday}{days}'

    return new_time
    

# print(add_time("3:30 PM", "2:12"), "\n👉 5:42 PM") # CHECK 12HR TIME
# print(add_time("11:55 AM", "3:12"), "\n👉 3:07 PM") # CHECK 12HR TIME
# print(add_time("9:15 PM", "5:30"), "\n👉 2:45 AM (next day)")
# print(add_time("11:40 AM", "0:25"), "\n👉 12:05 PM")
# print(add_time("2:59 AM", "24:00"), "\n👉 2:59 AM (next day)")
# print(add_time("11:59 PM", "24:05"), "\n👉 12:04 AM (2 days later)") # CHECK MERIDIAN
# print(add_time("8:16 PM", "466:02"), "\n👉 6:18 AM (20 days later)")
# print(add_time("5:01 AM", "0:00"),"\n👉 5:01 AM")

print(add_time("3:30 PM", "2:12", "Monday"), "\n👉 5:42 PM, Monday") # CHECK 12HR TIME
print(add_time("2:59 AM", "24:00", "saturDay"), "\n👉 2:59 AM, Sunday (next day)")
print(add_time("11:59 PM", "24:05", "Wednesday"), "\n👉 12:04 AM, Friday (2 days later)") # CHECK MERIDIAN
print(add_time("8:16 PM", "466:02", "tuesday"), "\n👉 6:18 AM, Monday (20 days later)") # CHECK DAY!!

print(add_time("8:16 AM", "24:00", "sunday"), "\n👉 8:16 AM, Monday (next day)") # CHECK DAY!!
print(add_time("8:16 PM", "24:00", "sunday"), "\n👉 8:16 PM, Monday (next day)") # CHECK DAY!!

print(add_time("8:16 PM", "240:02", "sunday"), "\n👉 8:18 PM, Wednesday (10 days later)") # CHECK DAY!!