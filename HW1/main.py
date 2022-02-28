import sys
from rich import print as rprint
import random

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
# Player Class
class Player:
    def __init__(self, characteristics: dict):
        self.pokemon = ""
        if(characteristics["pokemon"]) == "Chimchar":
            self.pokemon = Chimchar
        elif (characteristics["pokemon"]) == "Piplup":
            self.pokemon = Piplup
        elif (characteristics["pokemon"]) == "Turtwig":
            self.pokemon = Turtwig

        self.money = characteristics["money"]
        self.bag = characteristics["bag"]
        self.name = characteristics["name"]
        self.gender = characteristics["gender"]
        self.nature = characteristics["nature"]
        self.output_type = self.gender
        self.row = 0
        self.col = 0

    def __repr__(self):
        return self.gender

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
# Pokemon Class
class Pokemon:
    def __init__(self, stats: dict):
        self.name = stats["name"]
        self.hp = stats["hp"]
        self.gender = stats["gender"]
        self.nature = stats["nature"]
        self.moves = stats["moves"]
        self.output_type = "\U0001F47E"
        self.type = "pokemon"

    def __repr__(self):
        return "\U0001F47E"


Natures = {
    0: "Hardy",
    1: "Lonely",
    2: "Brave",
    3: "Adamant",
    4: "Naughty",
    5: "Bold",
    6: "Docile",
    7: "Relaxed",
    8: "Impish",
    9: "Lax",
    10: "Timid",
    11: "Hasty",
    12: "Serious",
    13: "Jolly",
    14: "Naive",
    15: "Modes",
    16: "Mild",
    17: "Quiet",
    18: "Bashful",
    19: "Rash",
    20: "Calm",
    21: "Gentle",
    22: "Sassy",
    23: "Careful",
    24: "Quirky"
}
Chimchar = Pokemon({
    "name": "Chimchar",
    "hp": 100,
    "gender": "M" if random.randrange(0, 2) == 0 else "F",
    "nature": Natures[random.randrange(0, 25)],
    "moves": {"Ember": 50, "Acrobatics": 40}
})

Piplup = Pokemon({
    "name": "Piplup",
    "hp": 100,
    "gender": "M" if random.randrange(0, 2) == 0 else "F",
    "nature": Natures[random.randrange(0, 25)],
    "moves": {"Bubble": 50, "Drill Peck": 40}
})

Turtwig = Pokemon({
    "name": "Turtwig",
    "hp": 100,
    "gender": "M" if random.randrange(0, 2) == 0 else "F",
    "nature": Natures[random.randrange(0, 25)],
    "moves": {"Razor Leaf": 50, "Bite": 40}
})

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
# CPU Trainer Class
class Trainer:
    def __init__(self, characteristics: dict):
        self.name = characteristics["name"]
        self.money_awarded = characteristics["money_awarded"]
        self.pokemon_gifted = characteristics["pokemon_gifted"]
        self.fun_fact = characteristics["fun_fact"]
        self.output_type = "\U0001F464"
        self.type = "trainer"

        if (characteristics["pokemon_gifted"]) == "Chimchar":
            self.pokemon = Chimchar
        elif (characteristics["pokemon_gifted"]) == "Piplup":
            self.pokemon = Piplup
        elif (characteristics["pokemon_gifted"]) == "Turtwig":
            self.pokemon = Turtwig

    def __repr__(self):
        return "\U0001F464"

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
# Tile Class
class Tile:
    def __init__(self, obj):
        self.stored_obj = obj

    def __repr__(self):
        if isinstance(self.stored_obj, str):
            return "\U0001F7E9"
        return self.stored_obj.output_type


# Grid Class
class Grid:
    def __init__(self):
        # \u25A0 -> ■
        # \u25D3 -> ◓
        # \U0001F464 -> 👤

        self.grid = [
            [Tile(player), Tile("N"), Tile("N"), Tile("N"), Tile(trainer3), Tile("N"), Tile("N"), Tile("N")],
            [Tile("N"), Tile("N"), Tile("N"), Tile("N"), Tile("N"), Tile("N"), Tile("N"), Tile("N")],
            [Tile("N"), Tile("N"), Tile(Chimchar), Tile("N"), Tile("N"), Tile(trainer2), Tile("N"), Tile("N")],
            [Tile(trainer4), Tile("N"), Tile("N"), Tile("N"), Tile("N"), Tile("N"), Tile("N"), Tile(Turtwig)],
            [Tile("N"), Tile("N"), Tile("N"), Tile("N"), Tile("N"), Tile("N"), Tile("N"), Tile("N")],
            [Tile("N"), Tile("N"), Tile("N"), Tile("N"), Tile(trainer1), Tile("N"), Tile("N"), Tile("N")],
            [Tile("N"), Tile(Piplup), Tile("N"), Tile("N"), Tile("N"), Tile("N"), Tile("N"), Tile("N")],
            [Tile("N"), Tile("N"), Tile("N"), Tile("N"), Tile("N"), Tile("N"), Tile(Chimchar), Tile("N")],
        ]

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
# Encounter
def encounter(encountered_obj, encountered_obj_row, encountered_obj_col):
    # If thing is pokemon, start a battle, return false if player loses, encountered_obj is a Pokemon
    if encountered_obj.type == "pokemon":
        print("----------------------------------------------------------")
        rprint(encountered_obj.output_type + f" A wild {encountered_obj.name} has appeared " + encountered_obj.output_type)
        remaining_hp = encountered_obj.hp
        print("----------------------------------------------------------")

        # Battle until someone loses
        while player.pokemon.hp > 0 and remaining_hp > 0:
            # player makes a move
            attack = input(f"Options: fight, run, or bag\n")
            print("----------------------------------------------------------")
            if attack == "run" and random.randrange(0, 2) == 0:
                rprint("You could not escape.")
                enemy_attack = random.choice(list(encountered_obj.moves))
                rprint(f"The enemy {encountered_obj.name} used {enemy_attack}")
                player.pokemon.hp -= encountered_obj.moves[enemy_attack]
                if player.pokemon.hp <= 0:
                    break
                rprint(f"Your {player.pokemon.name} has {player.pokemon.hp}/100 hp left")
                print("----------------------------------------------------------")
                continue
            elif attack == "run":
                rprint("You escaped")
                player.pokemon.hp = 100
                return

            elif attack == "bag":
                rprint(player.bag)
                bag_item = input("Pick an item to use\n")
                if bag_item == "Potion" and player.bag[bag_item] > 0:
                    player.pokemon.hp += 20
                    if player.pokemon.hp > 100:
                        player.pokemon.hp = 100
                    rprint(f"Your {player.pokemon.name} has {player.pokemon.hp}/100 hp left")

                # bad input
                else:
                    continue
                player.bag[bag_item] -= 1
                enemy_attack = random.choice(list(encountered_obj.moves))
                player.pokemon.hp -= encountered_obj.moves[enemy_attack]
                rprint(f"The enemy {encountered_obj.name} used {enemy_attack}")
                if player.pokemon.hp <= 0:
                    break
                rprint(f"Your {player.pokemon.name} has {player.pokemon.hp}/100 hp left")
                print("----------------------------------------------------------")
                continue

            elif attack == "fight":
                # List out player's attacks
                for k, v in player.pokemon.moves.items():
                    print(k + ": " + str(v) + " damage")
                print("----------------------------------------------------------")
                attack = input(f"Pick an attack for your {player.pokemon.name}\n")
                rprint(f"Your {player.pokemon.name} used {attack} ")
                remaining_hp -= player.pokemon.moves[attack]
                if remaining_hp <= 0:
                    break
                rprint(f"The enemy {encountered_obj.name} has {remaining_hp}/{encountered_obj.hp} hp left")
                print("----------------------------------------------------------")

                # enemy pokemon attacks
                enemy_attack = random.choice(list(encountered_obj.moves))
                player.pokemon.hp -= encountered_obj.moves[enemy_attack]
                rprint(f"The enemy {encountered_obj.name} used {enemy_attack}")
                if player.pokemon.hp <= 0:
                    break
                rprint(f"Your {player.pokemon.name} has {player.pokemon.hp}/100 hp left")
                print("----------------------------------------------------------")

            # bad input
            else:
                continue

    # If thing is trainer, start some battle but with some trainer dialogue maybe, return false if player loses, encounted_obj is a Trainer, need .pokemon
    if encountered_obj.type == "trainer":
        print("----------------------------------------------------------")
        rprint(encountered_obj.output_type + f" {encountered_obj.name} wants to battle " + encountered_obj.output_type)
        rprint(encountered_obj.fun_fact)
        rprint(f"{encountered_obj.name} sent out {encountered_obj.pokemon.name}")
        remaining_hp = encountered_obj.pokemon.hp
        print("----------------------------------------------------------")

        # Battle until someone loses
        while player.pokemon.hp > 0 and remaining_hp > 0:
            # player makes a move
            attack = input(f"Options: fight, run, or bag\n")
            print("----------------------------------------------------------")
            if attack == "run":
                rprint("You cannot run from a trainer battle.")
                print("----------------------------------------------------------")
                continue

            elif attack == "bag":
                rprint(player.bag)
                bag_item = input("Pick an item to use\n")
                if bag_item == "Potion" and player.bag[bag_item] > 0:
                    player.pokemon.hp += 20
                    if player.pokemon.hp > 100:
                        player.pokemon.hp = 100
                    rprint(f"Your {player.pokemon.name} has {player.pokemon.hp}/100 hp left")
                # bad input
                else:
                    continue
                player.bag[bag_item] -= 1
                enemy_attack = random.choice(list(encountered_obj.pokemon.moves))
                rprint(f"{encountered_obj.name}'s {encountered_obj.pokemon.name} used {enemy_attack}")
                player.pokemon.hp -= encountered_obj.pokemon.moves[enemy_attack]
                if player.pokemon.hp <= 0:
                    break
                rprint(f"Your {player.pokemon.name} has {player.pokemon.hp}/100 hp left")
                print("----------------------------------------------------------")
                continue


            elif attack == "fight":
                # List out player's attacks
                for k, v in player.pokemon.moves.items():
                    print(k + ": " + str(v) + " damage")

                attack = input(f"Pick an attack for your {player.pokemon.name}\n")
                print("----------------------------------------------------------")
                rprint(f"Your {player.pokemon.name} used {attack} ")
                remaining_hp -= player.pokemon.moves[attack]
                if remaining_hp <= 0:
                    break
                rprint(f"{encountered_obj.name}'s {encountered_obj.pokemon.name} has {remaining_hp}" + "/" + f"{encountered_obj.pokemon.hp} hp left")
                print("----------------------------------------------------------")

                # enemy pokemon attacks
                enemy_attack = random.choice(list(encountered_obj.pokemon.moves))
                rprint(f"{encountered_obj.name}'s {encountered_obj.pokemon.name} used {enemy_attack}")
                player.pokemon.hp -= encountered_obj.pokemon.moves[enemy_attack]
                if player.pokemon.hp <= 0:
                    break
                rprint(f"Your {player.pokemon.name} has {player.pokemon.hp}/100 hp left")
                print("----------------------------------------------------------")

            # bad input
            else:
                continue

    # player lost
    if player.pokemon.hp <= 0:
        rprint("Your pokemon is out of hp. Thank you for playing the early rendition of NOMEKOP")
        print("----------------------------------------------------------")
        sys.exit()
    # player won
    else:
        rprint("YOU WON, KEEP IT UP")
        print("----------------------------------------------------------")
        player.pokemon.hp = 100
        field.grid[encountered_obj_row][encountered_obj_col] = Tile("N")
        field.grid[player.row][player.col], field.grid[encountered_obj_row][encountered_obj_col] = field.grid[encountered_obj_row][encountered_obj_col], field.grid[player.row][player.col]
        player.row = encountered_obj_row
        player.col = encountered_obj_col
        if encountered_obj.type == "trainer":
            player.money += encountered_obj.money_awarded
            rprint(f"You now have {player.money} money")

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################


def game_loop():
    # Move around the board
    while True:
        # Take an input of up down left right
        move = input("Input a direction to move one space in: up, down, left, right (u,d,l,r also accepted)\n")
        # Check move is legal and perform if it is, but keep asking for new one if it is not
        while True:
            if (move == "u" or move == "up") and player.row-1 in range(0, 7):
                if not isinstance(field.grid[player.row - 1][player.col].stored_obj, str):
                    engage = input("There is something or someone on the space you are heading for. y or n to interact\n")
                    if engage == 'y':
                        encounter(field.grid[player.row - 1][player.col].stored_obj, player.row - 1, player.col)
                else:
                    # Swap player with space above
                    field.grid[player.row][player.col], field.grid[player.row-1][player.col] = field.grid[player.row-1][player.col], field.grid[player.row][player.col]
                    player.row -= 1
                break
            if (move == "d" or move == "down") and player.row+1 in range(1, 8):
                if not isinstance(field.grid[player.row + 1][player.col].stored_obj, str):
                    engage = input("There is something or someone on the space you are heading for. y or n to interact\n")
                    if engage == 'y':
                        encounter(field.grid[player.row + 1][player.col].stored_obj, player.row + 1, player.col)
                else:
                    # Swap player with space below
                    field.grid[player.row][player.col], field.grid[player.row+1][player.col] = field.grid[player.row+1][player.col], field.grid[player.row][player.col]
                    player.row += 1
                break
            if (move == "l" or move == "left") and player.col-1 in range(0, 7):
                if not isinstance(field.grid[player.row][player.col-1].stored_obj, str):
                    engage = input(
                        "There is something or someone on the space you are heading for. y or n to interact\n")
                    if engage == 'y':
                        encounter(field.grid[player.row][player.col - 1].stored_obj, player.row, player.col - 1)
                else:
                    field.grid[player.row][player.col], field.grid[player.row][player.col-1] = field.grid[player.row][player.col-1], field.grid[player.row][player.col]
                    player.col -= 1
                break
            if (move == "r" or move == "right") and player.col+1 in range(1, 8):
                if not isinstance(field.grid[player.row][player.col+1].stored_obj, str):
                    engage = input(
                        "There is something or someone on the space you are heading for. y or n to interact\n")
                    if engage == 'y':
                        encounter(field.grid[player.row][player.col + 1].stored_obj, player.row, player.col + 1)
                else:
                    field.grid[player.row][player.col], field.grid[player.row][player.col+1] = field.grid[player.row][player.col+1], field.grid[player.row][player.col]
                    player.col += 1
                break

            move = input("You inputted an illegal move, try again: up, down, left, right (u,d,l,r also accepted)\n")

        for row in field.grid:
            print(str(row).translate({39: None, 44: None, 91: None, 93: None}))


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
# Game Setup
rprint('WELCOME TO POKEMON CLONE NOMEKOP, FOLLOW THE PROMPTS TO PREPARE YOUR CHARACTER')
# "\U0001F468" -> 👨
# "\U0001F469" -> 👩
player_characteristics = {
    "pokemon": input("Enter a Starter Pokemon from the list: Chimchar, Piplup, Turtwig\n"),
    "money": int(input("Enter an amount of starter money\n")),
    "bag": {"Potion": 5},
    "name": input("Enter the name for your player\n"),
    "gender": "\U0001F468" if input("Enter the gender for your player: M or F\n") == "M" else "\U0001F469",
    "nature": input("Enter the nature for your player such as kind, mean, funny, empathetic, etc\n"),
}

# DEBUGGING
# player_characteristics = {
#     "pokemon": "Chimchar",
#     "money": 100,
#     "bag": {"Potion": 5},
#     "name": "Tom",
#     "gender": "\U0001F468",
#     "nature": "kind"
# }

trainer1_characteristics = {
    "name": "Jay",
    "money_awarded": 200,
    "pokemon_gifted":  "Chimchar",
    "fun_fact": "Jay enjoys bike riding"
}

trainer2_characteristics = {
    "name": "Emily",
    "money_awarded": 200,
    "pokemon_gifted":  "Piplup",
    "fun_fact": "Emily loves to hike on a beautiful day"
}

trainer3_characteristics = {
    "name": "Chelsea",
    "money_awarded": 200,
    "pokemon_gifted":  "Turtwig",
    "fun_fact": "Chelsea is out to win the big one"
}

trainer4_characteristics = {
    "name": "Tom",
    "money_awarded": 200,
    "pokemon_gifted":  "Piplup",
    "fun_fact": "Tom enjoys gaming with the peeps"
}

player = Player(player_characteristics)
trainer1 = Trainer(trainer1_characteristics)
trainer2 = Trainer(trainer2_characteristics)
trainer3 = Trainer(trainer3_characteristics)
trainer4 = Trainer(trainer4_characteristics)
field = Grid()

rprint("NOW ENTER THE WORLD OF NOMEKOP AND DEFEAT THEM ALL")

for row in field.grid:
    print(str(row).translate({39: None, 44: None, 91: None, 93: None}))
    # Format to remove chars:   '         ,         [         ]
    # The numbers are the ascii/unicodes for those chars


game_loop()
