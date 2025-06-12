"""
Prompt:

Design a parking lot access control system. Vehicles can enter and exit the parking lot, 
and each vehicle has a license plate, vehicle type (e.g., car, motorcycle, truck), and an
associated entry/exit timestamp. The parking lot has a fixed capacity, and different types of 
vehicles take up different numbers of spots (e.g., motorcycle = 1, car = 2, truck = 4).

You will receive a sequence of vehicle entry and exit events from a file. Your system should:

Track which vehicles are currently inside

Deny entry if there’s insufficient space

Log every entry and exit

Calculate the total amount of time each vehicle stayed (for billing purposes)

"""