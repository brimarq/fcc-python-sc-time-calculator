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

    m_in_day = 1440

    # Convert start hour to 24hr time
    start_h = start_h + 12 if start.split()[1] == 'PM' else start_h

    # Convert to minutes
    start_time = start_h * 60 + start_m
    dur_time = dur_h * 60 + dur_m
    target_time = start_time + dur_time

    
    num_days = target_time // m_in_day

    # Set days note if applicable 
    days = f' ({num_days} days later)' if num_days > 1 else ' (next day)' if num_days == 1 else ''

    dow = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    
    d = 0
    h = 0
    m = 0
    meridian = ''

    # Seperate target hours and minutes
    h = target_time // 60
    m = target_time % 60

    if h > 24:
        # print(h % 24)
        h %= 24

    # Set AM/PM
    meridian = 'PM' if h >= 12 else 'AM'

 
    # Convert hours to 12-hr time
    h = 12 if h == 0 else h - 12 if h > 12 else h

    

    if weekday:
        d = num_days
        start_index = dow.index(weekday.lower())

        if d > 7:
            d %= 7

        target_index = start_index + d
        
        if target_index >= len(dow): 
            weekday = ', ' + dow[target_index - len(dow)].capitalize()
        else:
            weekday = ', ' + dow[target_index].capitalize()
    

    new_time = f'{str(h)}:{str(m).zfill(2)} {meridian}{weekday}{days}'

    return new_time
    

print(add_time("3:30 PM", "2:12"), "\n👉 5:42 PM") # CHECK 12HR TIME
print(add_time("11:55 AM", "3:12"), "\n👉 3:07 PM") # CHECK 12HR TIME
print(add_time("9:15 PM", "5:30"), "\n👉 2:45 AM (next day)")
print(add_time("11:40 AM", "0:25"), "\n👉 12:05 PM")
print(add_time("2:59 AM", "24:00"), "\n👉 2:59 AM (next day)")
print(add_time("11:59 PM", "24:05"), "\n👉 12:04 AM (2 days later)") # CHECK MERIDIAN
print(add_time("8:16 PM", "466:02"), "\n👉 6:18 AM (20 days later)")
print(add_time("5:01 AM", "0:00"),"\n👉 5:01 AM")

print(add_time("3:30 PM", "2:12", "Monday"), "\n👉 5:42 PM, Monday") # CHECK 12HR TIME
print(add_time("2:59 AM", "24:00", "saturDay"), "\n👉 2:59 AM, Sunday (next day)")
print(add_time("11:59 PM", "24:05", "Wednesday"), "\n👉 12:04 AM, Friday (2 days later)") # CHECK MERIDIAN
print(add_time("8:16 PM", "466:02", "tuesday"), "\n👉 6:18 AM, Monday (20 days later)") # CHECK DAY!!

print(add_time("8:16 AM", "24:00", "sunday"), "\n👉 8:16 AM, Monday (next day)") # CHECK DAY!!
print(add_time("8:16 PM", "24:00", "sunday"), "\n👉 8:16 PM, Monday (next day)") # CHECK DAY!!

print(add_time("8:16 PM", "240:02", "sunday"), "\n👉 8:18 PM, Wednesday (10 days later)") # CHECK DAY!!