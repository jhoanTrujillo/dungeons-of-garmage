import sys,time,random
from rich import print

def event_handler(event, player):
  """
  use to handle the events a a more concie maner. It needs a player and
  choices file to read and function.
  """
  if event.is_ending == True:
      exit_game()
  
  if event.is_healing == True:
    message_on_healing = player.restore_damage()
    print(message_on_healing)
  elif event.is_damage == True:
    message_on_damage = player.take_damage()
    print(message_on_damage)

def exit_game():
  print("[red]Farewell, Wanderer...[/red]")
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
    #Ensures everything displays in the same line
    sys.stdout.flush()
    #Changes the rate at which each letter is displayed
    time.sleep(random.random()*15.0/typing_speed)
  print('') 


