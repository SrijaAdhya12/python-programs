def convert_time(time):
    meredian = time[-2:]
    new_time = time[:-2]
    hr = new_time[:2]
    if meredian == "AM" and hr == "12":
        return "00" + new_time[2:]
    if meredian == "PM" and hr == "12":
        return "12" + new_time[2:]
    if meredian == "AM":
        return new_time
    hrs = new_time.split(":")
    hours = int(hrs[0])
    hours_in_12 = hours+12
    hrs[0] = str(hours_in_12)
    return ":".join(hrs)
    

time = input("Enter time in 12 hours: ")
print(convert_time(time))
