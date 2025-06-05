CPS = [
    "MH04CC2", "MH04C2820", "MHO4BB3232", "MH04CC2113", "MHO4CC2878",
    "MHO4BB8", "MH04CC2888", "MH04CC1313", "MH04CC2222", "MH04C1201",
    "MH04CC555", "MH0406565", "MH04A7"
]


def valid_number(num):
    return 6<= len(num)<=12 and num.isalnum()  

def insert_car(car_num):
    if not valid_number(car_num):
        return "Not valid input"
    
    CPS.append(car_num)
    return f"CAR PARKED AT POSITION {len(CPS)}"


def find_car(car_number):
    if not valid_number(car_number):
        return "Car number is not valid"

    return f"CAR IS AT POSITION {CPS.index(car_number)+1}" if car_number in CPS else "CAR DOESNOT EXIST"
    
    # count = 1
    # for car in CPS:
    #     if car == car_number:
    #         return f"Car found at position {count}"
    #     count += 1
    
    # return "Car not found"


num = int(input("Enter option number: "))

if num == 1:
    car_number = input("Enter car number: ")
    print(insert_car(car_number))
elif num == 2:
    car_number = input("Enter the car number to be found: ")
    print(find_car(car_number))
