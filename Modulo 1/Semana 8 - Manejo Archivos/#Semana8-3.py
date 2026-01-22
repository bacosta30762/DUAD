import json

def read_pokemon():
    try:
        with open("pokemon.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_pokemon(pokemon):
    with open("pokemon.json", "w", encoding="utf-8") as file:
        json.dump(pokemon, file, indent=4, ensure_ascii=False)    


def add_pokemon():
    pokemon = read_pokemon()

    while True:
        print("Do yo want to add a pokemon?")
        print("1. Yes")
        print("2. No")

        choice = input("Enter choice (1 or 2): ")

        if choice == '2':
            print("Exiting program...")
            break    

        elif choice == '1':
            name = input("Name of the pokemon: ").strip()

            types = []
            while True:
                pokemon_type = input("Type (press ENTER to finish): ").strip()
                if pokemon_type == "":
                    break
                types.append(pokemon_type)

            base = {}
            stats = [
                "HP",
                "Attack",
                "Defense",
                "Sp. Attack",
                "Sp. Defense",
                "Speed"
            ]
            
            for stat in stats:
                while True:
                    try:
                        value = int(input(f"{stat}: "))
                        base[stat] = value
                        break
                    except ValueError:
                        print("Please enter a valid number")

            new_pokemon = {
                    "name": {
                        "english": name
                    },
                    "type": types,
                    "base": base
                }
            
            pokemon.append(new_pokemon)
            save_pokemon(pokemon)


            print("Pokemon added")
            continue
        
        else:
            print("Invalid option. Try again.")  


add_pokemon()  