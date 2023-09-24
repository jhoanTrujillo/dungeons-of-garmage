import sys,time,random
from rich import print

def str_validator(str):
  try:
    if type(str) != "str":
      raise ValueError("Please enter a value of (either 'y' or 'n').")
  except ValueError as e:
    print(e)
  else:
    return

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
    time.sleep(random.random()*10.0/typing_speed)
  print('') 