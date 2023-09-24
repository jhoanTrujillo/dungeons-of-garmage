from rich import print
from classess.choices import *
from utility.utility import *
from classess.player import player


#The main play option is found below.
def play(node):
    """
    Reads the nodes that handle the event print, and change the history
    based on the player choice.
    """
    print("""\n=============================================================\n""")
    event = node
    #Trim any white space from the string in the node object
    event_text = event.text.strip(" ")
    slow_print(event_text)
    #Checks for the variables in the node
    if event.is_ending == True:
        exit_game()
        
    if event.is_healing == True:
        message_on_healing = player.restore_damage()
        print(message_on_healing)

    if event.is_damage == True:
        message_on_damage = player.take_damage()
        print(message_on_damage)

    #Iterate over the choices the player can take and addes them to the menu.
    for i, (option, _) in enumerate(event.options, 1):
        print(f"{i}. {option}")

    try:
        choice = int(input("Enter (1 or 2) for options, any other button to leave: \n"))
    except ValueError:
        exit()

    #Assign a value equal to the next node given choices node
    next_node = event.options[choice - 1][1]
    play(next_node)

def start():
    """
    Read player input and allow access to play function if input is 'Y'
    """
    player_choice = str(input("Do you wish to continue? (Y/N):\n"))
    str_validator(player_choice)
    
    player_choice.lower()
    
    if player_choice == 'y':
        play(corridor)
    elif player_choice == 'n':
        exit_game()
    else: 
       print('[red bold]Please type either "y" to play or "n" to exit. [/ red bold]')
       start()

def main():
  """
  Holds the main game loop
  """
  #Game title
  print("""[green]===========================================================================[/green]""")
  print(r"""
  [green]
    ____                                                   ____   ______                                    
   / __ \__  ______  ____ ____  ____  ____  _____   ____  / __/  / ____/___ __________ ___  ____ _____ ____ 
  / / / / / / / __ \/ __ `/ _ \/ __ \/ __ \/ ___/  / __ \/ /_   / / __/ __ `/ ___/ __ `__ \/ __ `/ __ `/ _ \
 / /_/ / /_/ / / / / /_/ /  __/ /_/ / / / (__  )  / /_/ / __/  / /_/ / /_/ / /  / / / / / / /_/ / /_/ /  __/
/_____/\__,_/_/ /_/\__, /\___/\____/_/ /_/____/   \____/_/     \____/\__,_/_/  /_/ /_/ /_/\__,_/\__, /\___/ 
                  /____/                                                                       /____/     
  [/ green]
  """)
  print("You stand at the gates of a [purple]mysterious[/ purple] dungeon, [green]Do you wish to enter?[/ green]")
  print("""[green]===========================================================================[/green]""")
  #Game starts here 
  start()

main()