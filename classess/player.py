class Player:
  """
  Player class which will hold the health of the player
  and some other values that can be change during the game.
  """
  def __init__(self) -> None:
    self.health = 5
  
  def take_damage(self):
    self.health -= 1
    return f"[red bold]You took damage. Current Health: { self.health }[/red bold]."
  
  def restore_damage(self):
    self.health += 1
    return f"[green bold]Some damage was restored. Current Health: { self.health }[/green bold]."

player = Player()