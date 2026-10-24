import random
import requests

def get_pokemon_data(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return {
                "name": data["name"].lower(),
                "height": data["height"],
                "weight": data["weight"],
            }
        else:
            print(f"Error: Server responded with status code {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return None

def main():
    pokemon_pool = [1, 2, 3, 4, 5]
    chosen_id = random.choice(pokemon_pool)
    
    pokemon = get_pokemon_data(chosen_id)
    if not pokemon:
        print("Could not retrieve Pokémon data. Exiting game.")
        return

    print("--- Guess the Pokémon! ---")
    print(f"Height: {pokemon['height']}")
    print(f"Weight: {pokemon['weight']}")
    print("Choices: bulbasaur, ivysaur, venusaur, charmander, charmeleon")

    max_attempts = 3
    for attempt in range(1, max_attempts + 1):
        guess = input(f"Attempt {attempt}/{max_attempts} - Enter Pokémon name: ").lower()

        if guess == pokemon["name"]:
            print(f"Congratulations! You got it right: {pokemon["name"]}!")
            return
        else:
            print("Incorrect guess!")

    print(f"Game Over! The correct Pokémon was: {pokemon["name"]}")

main()