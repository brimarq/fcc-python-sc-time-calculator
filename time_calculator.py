def add_time(start, duration, weekday=''):

    # Parse input times
    start_h = int(start.split()[0].split(':')[0])
    start_m = int(start.split()[0].split(':')[1])
    dur_h = int(duration.split(':')[0])
    dur_m = int(duration.split(':')[1])

    # Convert start hour to 24hr time
    start_h = start_h + 12 if start.split()[1] == 'PM' else start_h

    # Convert to minutes
    start_time = start_h * 60 + start_m
    dur_time = dur_h * 60 + dur_m
    target_time = start_time + dur_time

    # Calculate # of days
    d = target_time // 1440  # minutes per day

    # Seperate target hours and minutes
    h = target_time // 60 if (target_time // 60) < 24 else (target_time // 60) % 24
    m = target_time % 60

    # Set AM/PM
    meridian = ' PM' if h >= 12 else ' AM'

    # Convert hours to 12-hr time
    h = 12 if h == 0 else h - 12 if h > 12 else h

    # Set days note if applicable 
    note_days = f' ({d} days later)' if d > 1 else ' (next day)' if d == 1 else ''
    # Find target weekday if requested
    if weekday:
        dow = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
        start_index = dow.index(weekday.lower())
        target_index = start_index + d if d < 7 else start_index + (d % 7)

        if target_index >= len(dow): 
            weekday = ', ' + dow[target_index - len(dow)].capitalize()
        else:
            weekday = ', ' + dow[target_index].capitalize()
    
    new_time = f'{str(h)}:{str(m).zfill(2)}{meridian}{weekday}{note_days}'

    return new_time
