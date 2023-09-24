import sys
from rich import print
import classess.choices

story_node = classess.choices

def play(node):
    """
    Reads the nodes that handle the event print, and change the history
    based on the player choice.
    """
    #Prints the text string from the story node called. 
    print(node.event)
    #Goes over the choice the player can make and adds prompt
    for i, (option, _) in enumerate(node.options, 1):
        print(f"{i}. {option}")
    choice = int(input("Enter the number of your choice: (1 or 2) \n"))
    next_node = node.options[choice - 1][1]
    play(next_node)

def start():
    """
    Read player input and allow access to play function if input is 'Y'
    """
    player_choice = input("Do you wish to continue? (Y/N):\n")
    if type(player_choice) == 'str':
        player_choice.lower()

    try:
        if type(player_choice) != str:
            raise ValueError("Please enter a value of (either 'y' or 'n').")
        elif player_choice == 'y':
            play(story_node.node1)
        elif player_choice == 'n':
            exit()
    except ValueError as e:
        print(e)
        start()

def exit():
   print("[red]Farewell, Wanderer...[/red]")
   sys.exit()

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