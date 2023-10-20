from players import Player

tictactoe_logo_ascii_art = """
888   d8b        888                   888                    
888   Y8P        888                   888                    
888              888                   888                    
888888888 .d8888b888888 8888b.  .d8888b888888 .d88b.  .d88b.  
888   888d88P"   888       "88bd88P"   888   d88""88bd8P  Y8b 
888   888888     888   .d888888888     888   888  88888888888 
Y88b. 888Y88b.   Y88b. 888  888Y88b.   Y88b. Y88..88PY8b.     
 "Y888888 "Y8888P "Y888"Y888888 "Y8888P "Y888 "Y88P"  "Y8888 
"""


grid_string = """
_____________
| 1 | 2 | 3 |
=============
| 4 | 5 | 6 |
=============
| 7 | 8 | 9 |
=============
"""

p_name1 = input("Enter player 1 name: ")
p_name2 = input("Enter player 2 name: ")

player1 = Player(p_name1)
player2 = Player(p_name2)

player_turn = 1
used_fields = []


def show_board() -> None:
    print(f"{player1.name} {player1.score} : {player2.score} {player2.name} ")
    print(grid_string)


def game():
    global player_turn, grid_string
    if player_turn == 1:
        grid_string = grid_string.replace(player1.get_field(), "X")

    print(grid_string)


game()


def replay():
    pass
