import copy
#Ejercicio 1
hotel_dictionary = {
    "name": " ",
    "stars_number": 0,
    "rooms": []
}

all_hotels = {}

hotels = int(input("Enter the number of hotels you wish to add: "))
counter = 0

while counter < hotels:
    hotel_name = input("Enter the name of the hotel: ")
    stars_number = int(input("Enter the number of stars (1-5): "))
    
    hotel_dictionary["name"] = hotel_name
    hotel_dictionary["stars_number"] = stars_number
    
    rooms = int(input("Enter the number of rooms in the hotel: "))
    room_counter = 0
    hotel_dictionary["rooms"] = []
    
    while room_counter < rooms:
        room_number = int(input("Enter the room number: "))
        room_floor = input("Enter the floor that the room is located: ")
        room_price = float(input("Enter the room price per night: "))
        
        room_info = {
            "room_number": room_number,
            "room_floor": room_floor,
            "room_price": room_price
        }
        
        hotel_dictionary["rooms"].append(room_info)
        room_counter += 1

    all_hotels[hotel_name] = copy.deepcopy(hotel_dictionary)
    
    print(f"Hotel added: {hotel_dictionary}")
    counter += 1

print(all_hotels)