"""
You're given user meeting data for each day of the week (Monday through Sunday). Each day maps to a list of meetings in the form of ISO 8601 time ranges.

All meetings are exactly 30 minutes long, and meetings can begin on the hour or half-hour within working hours.

You are asked to calculate, for each day, the number of unbooked 30-minute slots between 08:00 and 17:00 (inclusive of 16:30–17:00).
Constraints:
There are 18 total 30-minute slots per day:
08:00–08:30, 08:30–09:00, ..., 16:30–17:00
Each meeting is exactly 30 minutes and aligned to the hour or half-hour mark.
A slot is booked if it matches any start time in the list for that day.
"""

"""
Notes:
- unbooked time
- logic:
- convert the time -> string manipulation, we only care about the time numbers, write in format of 0800
- how do we look at unbooked time: have an array of available booking, pop ranges of values when booking are made
"""
class unbooked_times:
    def __init__(self, bookings):
        self.bookings = bookings
    def available_bookings(self):
        available_bookings = []
        current_time = "0800"
        closing_time="1700"
        while current_time < closing_time:
            available_bookings.append(current_time)
            minute = int(current_time[2:])
            hour = int(current_time[:2])

            minute += 30
            if minute >= 60:
                minute -= 60
                hour += 1

            current_time = f"{hour:02d}{minute:02d}"
        return available_bookings 
    def count_unbookedTime(self):
        available_bookings = self.available_bookings()
        count={}
        for day, day_bookings in self.bookings.items():
            for booking in day_bookings:
                start_time = booking[0].split("T")[1].replace(":","")[:4]
                end_time = booking[1].split("T")[1].replace(":","")[:4]
                if start_time in available_bookings:
                    available_bookings = [slot for slot in available_bookings if not (start_time <= slot < end_time)]
            count[day]=len(available_bookings)
        return count                 
            

bookings = {
    "Monday": [
        ("2024-03-04T08:00:00", "2024-03-04T09:00:00"),  # normal, 2 slots
        ("2024-03-04T10:45:00", "2024-03-04T11:15:00"),  # overlaps 2 slots
        ("2024-03-04T15:00:00", "2024-03-04T15:30:00"),  # exact 1 slot
        ("2024-03-04T16:59:00", "2024-03-04T17:00:00")   # edge: final minute of the day
    ],
    "Tuesday": [
        ("2024-03-05T09:30:00", "2024-03-05T10:45:00"),  # overlaps 3 slots
        ("2024-03-05T07:30:00", "2024-03-05T08:30:00"),  # partially outside working hours
        ("2024-03-05T12:00:00", "2024-03-05T12:29:00"),  # partial slot (round down)
        ("2024-03-05T12:31:00", "2024-03-05T12:59:00")   # partial slot (round up)
    ],
    "Wednesday": [
        ("2024-03-06T08:00:00", "2024-03-06T17:00:00")   # entire day booked
    ],
    "Thursday": [
        ("2024-03-07T08:15:00", "2024-03-07T08:45:00"),  # cuts across 1st slot
        ("2024-03-07T11:00:00", "2024-03-07T11:31:00"),  # 2 slots (one full, one partial)
        ("2024-03-07T16:00:00", "2024-03-07T17:00:00")   # last 2 slots
    ],
    "Friday": [
        ("2024-03-08T08:00:00", "2024-03-08T08:30:00"),
        ("2024-03-08T08:30:00", "2024-03-08T09:00:00"),
        ("2024-03-08T09:00:00", "2024-03-08T09:30:00"),
        ("2024-03-08T10:00:00", "2024-03-08T10:30:00"),
        ("2024-03-08T10:30:00", "2024-03-08T11:00:00"),
        ("2024-03-08T14:00:00", "2024-03-08T15:00:00"),  # 2 slots
        ("2024-03-08T15:00:00", "2024-03-08T15:15:00"),  # partial, inside above range
    ],
    "Saturday": [],
    "Sunday": [
        ("2024-03-10T08:00:00", "2024-03-10T08:15:00"),  # less than a slot
        ("2024-03-10T08:30:00", "2024-03-10T09:00:00"),
        ("2024-03-10T11:30:00", "2024-03-10T12:00:00"),
        ("2024-03-10T16:45:00", "2024-03-10T17:00:00")   # edge: partial end of day
    ]
}

# for day, day_booking in bookings.items():
#     for booking in day_booking:
#         print(booking[0].split("T")[1].replace(":","")[:4][2:])

first_set = unbooked_times(bookings)
print(first_set.count_unbookedTime())


