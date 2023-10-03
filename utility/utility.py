import sys,time,random
import classess.choices as event
from classess.characters import player, enemies
from rich import print

######################
### Game mechanics ###
######################

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
        """
        The play function should start with event.intro on production.
        For testing purpoe the intro object name can be change to any other node in the 
        choices module inside the classess folder
        """
        play(event.library)
    elif player_choice == 'n':
        exit_game()
    else: 
       print("[red ]Enter \"y\" to [bold]play[/ bold] or \"n\" to [bold]exit[/ bold].[/ red bold]")
       start()

def play(event_node):
    """
    Main game loop. Display event text, choices, and handle player choices.
    It also handles, damage, heal, and any other event logic.
    """
    print("\n[cyan]========================================================================[/ cyan]\n")
    #Checks for the event type, and handles the logic. If the player isn't dead. Display story text.
    event_handler(event_node)
    """
    Display the consequences of choices, and the dialog given to the event. 
    Listens for player choices and return the value selected by the player. 
    It also allows player to end the game. 
    """
    choice = event_choices(event_node)
    #Uses the choice variable to select the next node that will be display.
    next_node = event_node.options[choice- 1][1]
    play(next_node)

def event_choices(event_node):
  #Prints the dialog in the node given, in a human like way.
  #slow_print(event_node.text)
  print(event_node.text)
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

def event_handler(event_node):
  """
  use to handle the events a a more concie maner. It needs a player and
  choices file to read and function.
  """
  
  #Handle endings for the game. Ensures no options are display after text and ends game.
  if event_node.category == "ending":
    print(event_node.text)
    exit_game()
  #Display the text of a battle between enemy and player
  if event_node.category == "battle":
    #We refer to the enemis array 
    enemy_list = enemies
    #Since modules are unable to accept dot notation with variables holding strings. 
    #I'm using the array below and the .enemy_name string from the event node.
    enemy = enemy_list[event_node.enemy_name]
    #Then we call the battle function
    battle(player, enemy)
  #Handles the consequence of health reduce or gain from choices.
  if event_node.category == "healing":
    healing = player.restore_damage()
    print(healing)
  elif event_node.category == "damage":
    damage = player.take_damage()
    print(damage)

def battle(player, enemy):
    """
    As long as the player has health. Check for the damage
    calculation between the enemy and the player
    """
    #If the player is not dead. Do: 
    while player.is_dead != True:
      #Calculates and adds damage to enemy. Also, returns a string with an event message.
      player_attack = player.do_damage(enemy)
      print(player_attack)
      #If the enemy is not dead. Do:
      if enemy.is_dead != True:
          #Since enemy and player inherit from the character class this does the same as above.
          enemy_attack = enemy.do_damage(player)
          print(enemy_attack)
      #This breaks the loop if the enemy is_dead status is true
      else:
        slow_print(f"You defeated the {enemy.name}. Current health: {player.health}")
        #IMPORTANT: ensures the while loop stops when the enemy is defeated.
        break
    else:
       play(event.dead_by_battle)

#########################
### General functions ###
#########################
def exit_game():
  """
  Stop program using the sys module to avoid errors on closing
  """
  print("[red]Farewell...[/red]")
  #exits game without raising an error.
  sys.exit()

def slow_print(str):
  """
  Slows down the display of text in the screen to simulate a human typing
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