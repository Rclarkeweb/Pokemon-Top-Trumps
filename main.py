# Pokemon Top Trumps API Game

# Import Modules
import requests
import random
import time

# Introduce the game
print('Welcome to Pokemon Top trumps!')
print('The game is best-of-three (The first opponent to win 2 rounds)')

time.sleep(1.5)

# Ask the player if they want to read how the game is played
about_game = input('Do you want to read how the game works? Yes: Y or No: N: ').upper()

if about_game == 'Y' or about_game == 'YES':
    print('The game works by giving you a choice of three different Pokemons. You can then choose which Pokemon to \n'
          'play with. You will select a stat to play against the computers Pokemon. If your Pokemons stat is \n'
          'higher then you win that round! The game is best-of-3. Good luck!')
    time.sleep(6)

print('Lets play!')

time.sleep(1.5)

# Create function to generate a random Pokémon
def generate_pokemon():

    pokemon_id = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_id)
    response = requests.get(url)
    pokemon = response.json()

    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight']
    }


# Count number of wins by player or computer
player_won = 0
computer_won = 0

# Create a for loop to play for 3 rounds
for num in range(1, 4):
    print('---------------------------------------')
    # Print what round it is
    print('Round ', num)

    time.sleep(1.5)

    # Three random Pokémon assigned for player to choose from
    chosen_pokemon1 = generate_pokemon()
    chosen_pokemon2 = generate_pokemon()
    chosen_pokemon3 = generate_pokemon()

    # Show the player the three Pokémon options
    print('You have a choice of these Pokemons: 1 {}, 2 {}, 3 {}.'.format(chosen_pokemon1['name'],
                                                                          chosen_pokemon2['name'],
                                                                          chosen_pokemon3['name']))

    # Ask the player if they want to see the Pokémon stats before selecting one
    more_info = input('Do you want to see the Pokemons stats? Yes: Y or No: N: ').upper()

    # If the player wants to see the Pokémon stats, print them out, else continue
    if more_info == 'Y' or more_info == 'YES':
        print('The chosen Pokemons have the following stats:\n '
              '1 Name: {}, ID: {}, Height: {}, Weight: {}\n '
              '2 Name: {}, ID: {}, Height: {}, Weight: {},\n '
              '3 Name: {}, ID: {}, Height: {}, Weight: {}'.format(chosen_pokemon1['name'], chosen_pokemon1['id'], chosen_pokemon1['height'], chosen_pokemon1['weight'], chosen_pokemon2['name'], chosen_pokemon2['id'], chosen_pokemon2['height'], chosen_pokemon2['weight'], chosen_pokemon3['name'], chosen_pokemon3['id'], chosen_pokemon3['height'], chosen_pokemon3['weight']))
        time.sleep(2.4)

    # Ask the user to make a choice of which Pokémon to play with
    choose_pokemon = int(input('Which Pokemon do you want to play with? Number 1, 2 or 3: '))

    if choose_pokemon == 1:
        player_pokemon = chosen_pokemon1
    elif choose_pokemon == 2:
        player_pokemon = chosen_pokemon2
    elif choose_pokemon == 3:
        player_pokemon = chosen_pokemon3
    else:
        print('That\'s not an available choice. Please re-run the game!')
        exit()

    # Print out the players chosen Pokémon
    print('You chose the Pokemon: {}. It\'s stats are: ID: {}, Height: {}, Weight: {}'.format(player_pokemon['name'],
                                                                                              player_pokemon['id'],
                                                                                              player_pokemon['height'],
                                                                                              player_pokemon['weight']))


    # Ask the user which stat they want play with
    choose_stat = int(input('Which stat do you want to play with? 1: ID, 2: Height or 3: Weight. '
                            'Please type 1, 2 or 3: '))

    # Generate the computers Pokémon
    computer_choice = generate_pokemon()

    # Stop the game if the players Pokémon and computers Pokémon is the same
    if computer_choice['name'] == player_pokemon['name']:
        print('Oh no! You have both chosen the same Pokemon! Please re-run the game!')
        exit()

    # Generate player stat and give the computer the same stat
    if choose_stat == 1:
        chosen_stat = "ID: " + str(player_pokemon['id'])
        computer_chosen_stat = "ID is: " + str(computer_choice['id'])
        player_stat = player_pokemon['id']
        computer_stat = computer_choice['id']
    elif choose_stat == 2:
        chosen_stat = "Height: " + str(player_pokemon['height'])
        computer_chosen_stat = "Height is: " + str(computer_choice['height'])
        player_stat = player_pokemon['height']
        computer_stat = computer_choice['height']
    elif choose_stat == 3:
        chosen_stat = "Weight: " + str(player_pokemon['weight'])
        computer_chosen_stat = "Weight is: " + str(computer_choice['weight'])
        player_stat = player_pokemon['weight']
        computer_stat = computer_choice['weight']
    else:
        print('That\'s not an available choice. Please re-run the game!')
        exit()

    # Print the players Pokémon and chosen stat
    print('You chose to play {}\'s {}'.format(player_pokemon['name'], chosen_stat))

    time.sleep(2)

    # Compare the Pokémon stats
    print('The computers chosen Pokemon is: {} and their {}.'.format(computer_choice['name'], computer_chosen_stat))

    time.sleep(2)

    if player_stat > computer_stat:
        print('Player wins Round', num)
        player_won += 1
    elif player_stat < computer_stat:
        print('Computer wins Round', num)
        computer_won += 1
    elif player_stat == computer_stat:
        print('Its a draw!')
    else:
        print('There has been an error!')
        exit()


    time.sleep(2.4)

    # If the player or computer wins 2 rounds end the game and print the winner
    if player_won == 2:
        winner = 'Player'
        print('---------------------------------------')
        print('The winner is: {}. Well done!'.format(winner))
        exit()
    elif computer_won == 2:
        winner = 'Computer'
        print('---------------------------------------')
        print('The winner is: {}. Better luck next time!'.format(winner))
        exit()

print('Game Over!')
