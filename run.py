from rich import print
import classess.choices as event
import utility.utility as util
import classess.characters as chars


#The main play option is found below.
def play(event_node):
    """
    Main game loop. Display event text, choices, and handle player choices.
    It also handles, damage, heal, and any other event logic.
    """
    print("""\n[cyan]========================================================================[/ cyan]\n""")
    #Trim any white space from the string in the node object
    event_text = event_node.text.strip(" ")
    util.slow_print(event_text)
    util.event_handler(event_node, chars.player)
    #Space for aesthetic purposes.
    print("\n")
    #Iterate over the choices the player can take and addes them to the menu.
    for i, (option, _) in enumerate(event_node.options, 1):
        print(f"{i}. {option}")

    try:
        choice = int(input("\nEnter (1 or 2) for your choice, or enter any other value to exit: \n"))
    except ValueError:
        util.exit_game()

    #Assign a value equal to the next node given choices node
    next_node = event_node.options[choice - 1][1]
    play(next_node)

def start():
    """
    Takes the player input, it force the input to become a string. 
    To prevent error and then triggers the initial event node to get started.
    Holds the choice loop
    """
    player_choice = str(input("Do you wish to continue? (Y/N):\n"))
    player_choice.lower()

    #If statement to validate the information
    if player_choice == 'y':
        play(event.corridor)
    elif player_choice == 'n':
        util.exit_game()
    else: 
       print("[red bold]Enter \"y\" to play or \"n\" to exit.[/ red bold]")
       start()

def main():
  """
  Initial function holds the game start function.
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