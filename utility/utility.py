import sys,time,random
import classess.choices as event
from classess.characters import player, enemies
from rich import print

def start():
    """
    Gets player input and force it into a string to eliminate type errors.
    Then Ask for a value to start or exit the game. If value isn't expected,
    then it will prompt a message and recall the function. 
    """
    #force value into string
    player_choice = str(input("Do you wish to continue? (y/n):\n"))
    player_choice.lower()

    #Checks value, to apply logic.
    if player_choice == 'y':
        play(event.intro)
    elif player_choice == 'n':
        exit_game()
    else: 
       print("[red ]Enter \"y\" to [bold]play[/ bold] or \"n\" to [bold]exit[/ bold].[/ red bold]")
       start()

#The main play option is found below.
def play(event_node):
    """
    Main game loop. Display event text, choices, and handle player choices.
    It also handles, damage, heal, and any other event logic.
    """
    print("""\n[cyan]========================================================================[/ cyan]\n""")
    #Checks for the event type, and handles the logic. If the player isn't dead. Display story text.
    event_handler(event_node)
    #Display the consequences of choices, and the dialog given to the event. 
    #Listens for player choices and return the value selected by the player. 
    #It also allows player to end the game. 
    choice = event_choices(event_node)
    #Uses the choice variable to select the next node that will be display.
    next_node = event_node.options[choice- 1][1]
    play(next_node)

def event_choices(event_node):
  event_text = event_node.text
  if event_node.type_of == "ending":
     print(event_node.text)
  else:
    slow_print(event_text)

  #Space for aesthetic purposes.
  print("\n")
  #Iterate over the choices the player can take and addes them to the menu.
  for i, (option, _) in enumerate(event_node.options, 1):
    slow_print(f"{i}. {option}")
  #Checks choice type
  try:
    choice = int(input("\nEnter (1 or 2) for your choice, or enter any other value to exit: \n"))
  except ValueError:
    exit_game()

  return choice

def event_handler(event):
  """
  use to handle the events a a more concie maner. It needs a player and
  choices file to read and function.
  """

  if event.type_of == "ending":
    print(f"[blue]And like that does the legend of {player.name} ends.[/ blue]")
    exit_game()

  if event.type_of == "battle":
    for enemy_name in enemies:
      if event.enemy_name == enemy_name:
        player.battle(enemy_name)

  if event.type_of == "healing":
    message_on_healing = player.restore_damage()
    print(message_on_healing)
  elif event.type_of == "healing":
    message_on_damage = player.take_damage()
    print(message_on_damage)

def exit_game():
  """
  Ends game
  """
  print("[red]Farewell...[/red]")
  #exits game without raising an error.
  sys.exit()

def slow_print(str):
  """
  Display text slower in the terminal. Provides a hand typed feeling to the text.
  This will help with user readability.
  """
  typing_speed = 200
  #Iterate over each letter of the str argument
  for letter in str:
    #uses system module to display letter in line
    sys.stdout.write(letter)
    #It avoids data from being display in the next line.
    sys.stdout.flush()
    #Changes the rate at which each letter is displayed
    time.sleep(random.random()*15.0/typing_speed)
  print('') 